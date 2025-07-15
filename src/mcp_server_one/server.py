"""
Servidor MCP principal com FastMCP
"""
import asyncio
import json
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP, Context
from mcp.types import TextContent, Resource, Tool

from .api_client import APIManager


# Contexto da aplicação
class AppContext:
    """Contexto da aplicação com APIs"""
    
    def __init__(self, api_manager: APIManager):
        self.api_manager = api_manager


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Gerencia o ciclo de vida da aplicação"""
    api_manager = APIManager()
    try:
        yield AppContext(api_manager=api_manager)
    finally:
        await api_manager.close()


# Criar servidor MCP
mcp = FastMCP(
    name="MCP Server One",
    lifespan=app_lifespan
)


# ==================== RESOURCES ====================

@mcp.resource("posts://all")
def get_all_posts_resource() -> str:
    """Recurso com todos os posts do JSONPlaceholder"""
    return json.dumps({
        "description": "Todos os posts do JSONPlaceholder",
        "endpoint": "https://jsonplaceholder.typicode.com/posts",
        "type": "posts_collection"
    }, indent=2)


@mcp.resource("posts://{post_id}")
def get_post_resource(post_id: str) -> str:
    """Recurso com informações de um post específico"""
    return json.dumps({
        "description": f"Post {post_id} do JSONPlaceholder",
        "endpoint": f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        "type": "single_post"
    }, indent=2)


@mcp.resource("users://all")
def get_users_resource() -> str:
    """Recurso com todos os usuários"""
    return json.dumps({
        "description": "Todos os usuários do JSONPlaceholder",
        "endpoint": "https://jsonplaceholder.typicode.com/users",
        "type": "users_collection"
    }, indent=2)


@mcp.resource("api://status")
def get_api_status() -> str:
    """Status das APIs disponíveis"""
    return json.dumps({
        "apis": {
            "jsonplaceholder": {
                "name": "JSONPlaceholder",
                "base_url": "https://jsonplaceholder.typicode.com",
                "description": "API fake para posts, usuários, comentários e todos",
                "endpoints": ["/posts", "/users", "/comments", "/todos"]
            },
            "catfacts": {
                "name": "Cat Facts",
                "base_url": "https://catfact.ninja",
                "description": "API de fatos sobre gatos",
                "endpoints": ["/fact", "/facts"]
            },
            "jokes": {
                "name": "Official Joke API",
                "base_url": "https://official-joke-api.appspot.com",
                "description": "API de piadas",
                "endpoints": ["/random_joke", "/jokes/{type}/random"]
            }
        }
    }, indent=2)


# ==================== TOOLS ====================

@mcp.tool()
async def get_posts(limit: Optional[int] = None, ctx: Context = None) -> str:
    """Busca posts do JSONPlaceholder"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        posts = await app_ctx.api_manager.jsonplaceholder.get_posts(limit)
        
        if ctx:
            await ctx.info(f"Buscando {len(posts)} posts")
        
        return json.dumps(posts, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar posts: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_post_by_id(post_id: int, ctx: Context = None) -> str:
    """Busca um post específico pelo ID"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        post = await app_ctx.api_manager.jsonplaceholder.get_post(post_id)
        
        if ctx:
            await ctx.info(f"Buscando post {post_id}")
        
        return json.dumps(post, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar post {post_id}: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_users(ctx: Context = None) -> str:
    """Busca todos os usuários"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        users = await app_ctx.api_manager.jsonplaceholder.get_users()
        
        if ctx:
            await ctx.info(f"Buscando {len(users)} usuários")
        
        return json.dumps(users, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar usuários: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_user_by_id(user_id: int, ctx: Context = None) -> str:
    """Busca um usuário específico pelo ID"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        user = await app_ctx.api_manager.jsonplaceholder.get_user(user_id)
        
        if ctx:
            await ctx.info(f"Buscando usuário {user_id}")
        
        return json.dumps(user, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar usuário {user_id}: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_todos(user_id: Optional[int] = None, ctx: Context = None) -> str:
    """Busca todos os todos (opcionalmente de um usuário específico)"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        todos = await app_ctx.api_manager.jsonplaceholder.get_todos(user_id)
        
        if ctx:
            if user_id:
                await ctx.info(f"Buscando todos do usuário {user_id}")
            else:
                await ctx.info(f"Buscando todos os todos ({len(todos)} encontrados)")
        
        return json.dumps(todos, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar todos: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def create_post(title: str, body: str, user_id: int, ctx: Context = None) -> str:
    """Cria um novo post (simulado)"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        post = await app_ctx.api_manager.jsonplaceholder.create_post(title, body, user_id)
        
        if ctx:
            await ctx.info(f"Post criado com sucesso (simulado)")
        
        return json.dumps(post, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao criar post: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_cat_fact(ctx: Context = None) -> str:
    """Busca um fato aleatório sobre gatos"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        fact = await app_ctx.api_manager.catfacts.get_random_fact()
        
        if ctx:
            await ctx.info("Buscando fato sobre gatos")
        
        return json.dumps(fact, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar fato sobre gatos: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_multiple_cat_facts(limit: int = 5, ctx: Context = None) -> str:
    """Busca múltiplos fatos sobre gatos"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        facts = await app_ctx.api_manager.catfacts.get_facts(limit)
        
        if ctx:
            await ctx.info(f"Buscando {limit} fatos sobre gatos")
        
        return json.dumps(facts, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar fatos sobre gatos: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_random_joke(ctx: Context = None) -> str:
    """Busca uma piada aleatória"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        joke = await app_ctx.api_manager.jokes.get_random_joke()
        
        if ctx:
            await ctx.info("Buscando piada aleatória")
        
        return json.dumps(joke, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar piada: {str(e)}")
        return f"Erro: {str(e)}"


@mcp.tool()
async def get_jokes_by_type(joke_type: str, ctx: Context = None) -> str:
    """Busca piadas por tipo (programming, general, knock-knock, etc.)"""
    try:
        app_ctx = mcp.get_context().request_context.lifespan_context
        jokes = await app_ctx.api_manager.jokes.get_jokes_by_type(joke_type)
        
        if ctx:
            await ctx.info(f"Buscando piadas do tipo: {joke_type}")
        
        return json.dumps(jokes, indent=2)
    except Exception as e:
        if ctx:
            await ctx.error(f"Erro ao buscar piadas do tipo {joke_type}: {str(e)}")
        return f"Erro: {str(e)}"


# ==================== PROMPTS ====================

@mcp.prompt()
def analyze_post(post_id: int) -> str:
    """Prompt para análise de um post específico"""
    return f"""
Analise o post {post_id} do JSONPlaceholder.

Primeiro, use a ferramenta get_post_by_id para buscar o post.
Depois, forneça uma análise detalhada incluindo:
1. Resumo do conteúdo
2. Sentimento geral
3. Principais temas abordados
4. Qualidade da escrita
5. Sugestões de melhoria

Por favor, seja detalhado e construtivo na análise.
"""


@mcp.prompt()
def user_profile_analysis(user_id: int) -> str:
    """Prompt para análise de perfil de usuário"""
    return f"""
Analise o perfil do usuário {user_id} do JSONPlaceholder.

Use estas ferramentas em sequência:
1. get_user_by_id para buscar informações do usuário
2. get_todos para buscar os todos do usuário (user_id={user_id})

Baseado nas informações obtidas, forneça:
1. Resumo do perfil pessoal
2. Análise dos todos (completados vs. pendentes)
3. Insights sobre produtividade
4. Sugestões para melhoria da organização

Seja profissional e construtivo na análise.
"""


@mcp.prompt()
def daily_inspiration() -> str:
    """Prompt para inspiração diária"""
    return """
Crie uma mensagem de inspiração diária usando nossos recursos.

Execute estas etapas:
1. Use get_cat_fact para adicionar um fato interessante sobre gatos
2. Use get_random_joke para adicionar um toque de humor

Combine tudo em uma mensagem motivacional que inclua:
- Um fato curioso sobre gatos para despertar interesse
- Uma piada para alegrar o dia
- Uma mensagem positiva e energética

Mantenha um tom positivo e energético!
"""


def main():
    """Função principal para executar o servidor"""
    import sys
    
    # Configurar argumentos da linha de comando
    if len(sys.argv) > 1:
        if sys.argv[1] == "--transport":
            transport = sys.argv[2] if len(sys.argv) > 2 else "sse"
        else:
            transport = "stdio"
    else:
        transport = "stdio"
    
    # Executar servidor
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Cliente de exemplo para testar o MCP Server One
"""
import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


async def test_server():
    """Testa o servidor MCP"""
    print("🚀 Testando MCP Server One...")
    
    # Configurar parâmetros do servidor
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "mcp-server-one"]
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Inicializar conexão
                await session.initialize()
                print("✅ Conexão estabelecida com sucesso!")
                
                # Testar recursos
                print("\n📋 Testando recursos...")
                resources = await session.list_resources()
                print(f"Recursos disponíveis: {len(resources.resources)}")
                for resource in resources.resources:
                    print(f"  - {resource.uri}: {resource.description}")
                
                # Testar ferramentas
                print("\n🔧 Testando ferramentas...")
                tools = await session.list_tools()
                print(f"Ferramentas disponíveis: {len(tools.tools)}")
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")
                
                # Testar prompts
                print("\n💬 Testando prompts...")
                prompts = await session.list_prompts()
                print(f"Prompts disponíveis: {len(prompts.prompts)}")
                for prompt in prompts.prompts:
                    print(f"  - {prompt.name}: {prompt.description}")
                
                # Testar algumas ferramentas
                print("\n🧪 Testando ferramentas específicas...")
                
                # Testar busca de posts
                print("\n1. Buscando posts...")
                try:
                    result = await session.call_tool("get_posts", {"limit": 3})
                    posts = json.loads(result.content[0].text)
                    print(f"   Posts encontrados: {len(posts)}")
                    if posts:
                        print(f"   Primeiro post: {posts[0]['title']}")
                except Exception as e:
                    print(f"   Erro: {e}")
                
                # Testar fato sobre gatos
                print("\n2. Buscando fato sobre gatos...")
                try:
                    result = await session.call_tool("get_cat_fact", {})
                    fact = json.loads(result.content[0].text)
                    print(f"   Fato: {fact.get('fact', 'N/A')}")
                except Exception as e:
                    print(f"   Erro: {e}")
                
                # Testar piada aleatória
                print("\n3. Buscando piada aleatória...")
                try:
                    result = await session.call_tool("get_random_joke", {})
                    joke = json.loads(result.content[0].text)
                    print(f"   Setup: {joke.get('setup', 'N/A')}")
                    print(f"   Punchline: {joke.get('punchline', 'N/A')}")
                except Exception as e:
                    print(f"   Erro: {e}")
                
                # Testar leitura de recurso
                print("\n4. Testando leitura de recurso...")
                try:
                    from mcp.types import AnyUrl
                    resource = await session.read_resource(AnyUrl("api://status"))
                    api_status = json.loads(resource.contents[0].text)
                    print(f"   APIs disponíveis: {len(api_status['apis'])}")
                    for api_name in api_status['apis'].keys():
                        print(f"     - {api_name}")
                except Exception as e:
                    print(f"   Erro: {e}")
                
                # Testar prompt
                print("\n5. Testando prompt...")
                try:
                    prompt = await session.get_prompt("daily_inspiration", {})
                    print(f"   Prompt: {prompt.messages[0].content.text[:100]}...")
                except Exception as e:
                    print(f"   Erro: {e}")
                
                print("\n🎉 Todos os testes concluídos!")
                
    except Exception as e:
        print(f"❌ Erro ao conectar com o servidor: {e}")
        print("Certifique-se de que o servidor está configurado corretamente.")


async def interactive_test():
    """Teste interativo com o servidor"""
    print("🔄 Modo interativo - Digite 'quit' para sair")
    
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "mcp-server-one"]
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                while True:
                    print("\n" + "="*50)
                    print("Opções:")
                    print("1. Listar recursos")
                    print("2. Listar ferramentas")
                    print("3. Listar prompts")
                    print("4. Buscar posts")
                    print("5. Fato sobre gatos")
                    print("6. Piada aleatória")
                    print("7. Status das APIs")
                    print("quit - Sair")
                    
                    choice = input("\nEscolha uma opção: ").strip()
                    
                    if choice.lower() == 'quit':
                        break
                    
                    try:
                        if choice == '1':
                            resources = await session.list_resources()
                            print(f"\n📋 Recursos ({len(resources.resources)}):")
                            for r in resources.resources:
                                print(f"  - {r.uri}: {r.description}")
                        
                        elif choice == '2':
                            tools = await session.list_tools()
                            print(f"\n🔧 Ferramentas ({len(tools.tools)}):")
                            for t in tools.tools:
                                print(f"  - {t.name}: {t.description}")
                        
                        elif choice == '3':
                            prompts = await session.list_prompts()
                            print(f"\n💬 Prompts ({len(prompts.prompts)}):")
                            for p in prompts.prompts:
                                print(f"  - {p.name}: {p.description}")
                        
                        elif choice == '4':
                            limit = input("Limite de posts (padrão: 5): ").strip()
                            limit = int(limit) if limit.isdigit() else 5
                            result = await session.call_tool("get_posts", {"limit": limit})
                            posts = json.loads(result.content[0].text)
                            print(f"\n📝 Posts ({len(posts)}):")
                            for post in posts:
                                print(f"  - {post['title']}")
                        
                        elif choice == '5':
                            result = await session.call_tool("get_cat_fact", {})
                            fact = json.loads(result.content[0].text)
                            print(f"\n🐱 Fato sobre gatos:")
                            print(f"  {fact.get('fact', 'N/A')}")
                        
                        elif choice == '6':
                            result = await session.call_tool("get_random_joke", {})
                            joke = json.loads(result.content[0].text)
                            print(f"\n😄 Piada:")
                            print(f"  {joke.get('setup', 'N/A')}")
                            print(f"  {joke.get('punchline', 'N/A')}")
                        
                        elif choice == '7':
                            from mcp.types import AnyUrl
                            resource = await session.read_resource(AnyUrl("api://status"))
                            status = json.loads(resource.contents[0].text)
                            print(f"\n📊 Status das APIs:")
                            for name, info in status['apis'].items():
                                print(f"  - {info['name']}: {info['description']}")
                        
                        else:
                            print("❌ Opção inválida!")
                    
                    except Exception as e:
                        print(f"❌ Erro: {e}")
                
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
    
    print("\n👋 Até logo!")


async def main():
    """Função principal"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        await interactive_test()
    else:
        await test_server()


if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python3
"""
Script simples para executar o servidor sem MCP
"""
import asyncio
import json
import httpx
from typing import Dict, Any, Optional


class SimpleAPIServer:
    """Servidor simples para testar as APIs"""
    
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def close(self):
        await self.client.aclose()
    
    async def get_posts(self, limit: Optional[int] = None) -> Dict[str, Any]:
        """Busca posts do JSONPlaceholder"""
        response = await self.client.get("https://jsonplaceholder.typicode.com/posts")
        posts = response.json()
        if limit:
            posts = posts[:limit]
        return {"posts": posts, "count": len(posts)}
    
    async def get_cat_fact(self) -> Dict[str, Any]:
        """Busca fato sobre gatos"""
        response = await self.client.get("https://catfact.ninja/fact")
        return response.json()
    
    async def get_random_joke(self) -> Dict[str, Any]:
        """Busca piada aleatória"""
        response = await self.client.get("https://official-joke-api.appspot.com/random_joke")
        return response.json()


async def test_apis():
    """Testa todas as APIs"""
    server = SimpleAPIServer()
    
    try:
        print("🚀 Testando APIs...")
        
        # Testar posts
        print("\n📝 Testando posts...")
        posts = await server.get_posts(limit=3)
        print(f"Posts encontrados: {posts['count']}")
        if posts['posts']:
            print(f"Primeiro post: {posts['posts'][0]['title']}")
        
        # Testar fatos sobre gatos
        print("\n🐱 Testando fatos sobre gatos...")
        fact = await server.get_cat_fact()
        print(f"Fato: {fact.get('fact', 'N/A')}")
        
        # Testar piadas
        print("\n😄 Testando piadas...")
        joke = await server.get_random_joke()
        print(f"Setup: {joke.get('setup', 'N/A')}")
        print(f"Punchline: {joke.get('punchline', 'N/A')}")
        
        print("\n🎉 Todos os testes passaram!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    finally:
        await server.close()


if __name__ == "__main__":
    asyncio.run(test_apis())

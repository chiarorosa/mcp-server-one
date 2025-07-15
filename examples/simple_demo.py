#!/usr/bin/env python3
"""
Exemplo de uso simples do MCP Server One
"""
import asyncio
import json
import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from mcp_server_one.api_client import APIManager
    print("✅ Importação bem-sucedida!")
    
    async def demo():
        """Demonstração das funcionalidades"""
        print("\n🚀 Demonstração do MCP Server One")
        print("=" * 50)
        
        async with APIManager() as api:
            try:
                # Testar JSONPlaceholder
                print("\n📝 1. Testando JSONPlaceholder API...")
                posts = await api.jsonplaceholder.get_posts(limit=3)
                print(f"   Posts encontrados: {len(posts)}")
                for post in posts:
                    print(f"   - {post['title']}")
                
                # Testar usuários
                print("\n👥 2. Testando usuários...")
                users = await api.jsonplaceholder.get_users()
                print(f"   Usuários encontrados: {len(users)}")
                for user in users[:3]:
                    print(f"   - {user['name']} ({user['email']})")
                
                # Testar fatos sobre gatos
                print("\n🐱 3. Testando Cat Facts API...")
                fact = await api.catfacts.get_random_fact()
                print(f"   Fato: {fact.get('fact', 'N/A')}")
                
                # Testar piadas
                print("\n😄 4. Testando Official Joke API...")
                joke = await api.jokes.get_random_joke()
                print(f"   Setup: {joke.get('setup', 'N/A')}")
                print(f"   Punchline: {joke.get('punchline', 'N/A')}")
                
                print("\n🎉 Demonstração concluída com sucesso!")
                
            except Exception as e:
                print(f"❌ Erro durante demonstração: {e}")
    
    if __name__ == "__main__":
        asyncio.run(demo())
        
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("Certifique-se de que as dependências estão instaladas:")
    print("  uv sync")
    sys.exit(1)

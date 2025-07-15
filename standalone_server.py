#!/usr/bin/env python3
"""
Servidor MCP Server One Standalone
"""
import sys
import os
import asyncio
import json
from contextlib import asynccontextmanager
from typing import AsyncIterator

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from mcp_server_one.api_client import APIManager
    
    print("🚀 MCP Server One - Servidor Independente")
    print("=" * 50)
    
    class StandaloneServer:
        """Servidor independente para testes"""
        
        def __init__(self):
            self.api_manager = None
        
        async def start(self):
            """Inicializa o servidor"""
            self.api_manager = APIManager()
            print("✅ Servidor iniciado com sucesso!")
            
            # Testar conectividade
            await self.test_connectivity()
        
        async def stop(self):
            """Para o servidor"""
            if self.api_manager:
                await self.api_manager.close()
                print("👋 Servidor parado")
        
        async def test_connectivity(self):
            """Testa conectividade com as APIs"""
            print("\n🔍 Testando conectividade...")
            
            try:
                # Testar JSONPlaceholder
                posts = await self.api_manager.jsonplaceholder.get_posts(limit=1)
                print(f"✅ JSONPlaceholder: {len(posts)} posts")
                
                # Testar Cat Facts
                fact = await self.api_manager.catfacts.get_random_fact()
                print(f"✅ Cat Facts: {len(fact.get('fact', ''))} caracteres")
                
                # Testar Jokes
                joke = await self.api_manager.jokes.get_random_joke()
                print(f"✅ Jokes: {joke.get('type', 'N/A')} joke")
                
                print("🎉 Todas as APIs estão funcionando!")
                
            except Exception as e:
                print(f"❌ Erro ao testar APIs: {e}")
        
        async def run_interactive(self):
            """Executa o servidor em modo interativo"""
            print("\n" + "=" * 50)
            print("Modo interativo - Digite 'quit' para sair")
            print("Comandos disponíveis:")
            print("  posts - Buscar posts")
            print("  users - Buscar usuários")
            print("  cat - Fato sobre gatos")
            print("  joke - Piada aleatória")
            print("  status - Status das APIs")
            print("  quit - Sair")
            
            while True:
                try:
                    command = input("\n> ").strip().lower()
                    
                    if command == 'quit':
                        break
                    
                    elif command == 'posts':
                        posts = await self.api_manager.jsonplaceholder.get_posts(limit=5)
                        print(f"\n📝 Posts ({len(posts)}):")
                        for post in posts:
                            print(f"  - {post['title']}")
                    
                    elif command == 'users':
                        users = await self.api_manager.jsonplaceholder.get_users()
                        print(f"\n👥 Usuários ({len(users)}):")
                        for user in users[:5]:
                            print(f"  - {user['name']} ({user['email']})")
                    
                    elif command == 'cat':
                        fact = await self.api_manager.catfacts.get_random_fact()
                        print(f"\n🐱 Fato sobre gatos:")
                        print(f"  {fact.get('fact', 'N/A')}")
                    
                    elif command == 'joke':
                        joke = await self.api_manager.jokes.get_random_joke()
                        print(f"\n😄 Piada:")
                        print(f"  {joke.get('setup', 'N/A')}")
                        print(f"  {joke.get('punchline', 'N/A')}")
                    
                    elif command == 'status':
                        print("\n📊 Status das APIs:")
                        print("  ✅ JSONPlaceholder - https://jsonplaceholder.typicode.com")
                        print("  ✅ Cat Facts - https://catfact.ninja")
                        print("  ✅ Official Joke API - https://official-joke-api.appspot.com")
                    
                    else:
                        print(f"❌ Comando desconhecido: {command}")
                
                except KeyboardInterrupt:
                    print("\n👋 Interrompido pelo usuário")
                    break
                except Exception as e:
                    print(f"❌ Erro: {e}")
    
    async def main():
        """Função principal"""
        server = StandaloneServer()
        
        try:
            await server.start()
            
            # Modo interativo se não há argumentos
            if len(sys.argv) == 1:
                await server.run_interactive()
            else:
                print("🎯 Servidor pronto para uso!")
                print("Use 'python standalone_server.py' para modo interativo")
        
        except KeyboardInterrupt:
            print("\n⚠️  Servidor interrompido pelo usuário")
        except Exception as e:
            print(f"❌ Erro: {e}")
        finally:
            await server.stop()
    
    if __name__ == "__main__":
        asyncio.run(main())
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("Certifique-se de que as dependências estão instaladas:")
    print("  uv sync")
    sys.exit(1)

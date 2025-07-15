#!/usr/bin/env python3
"""
Teste simples do servidor
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from mcp_server_one.api_client import APIManager
    print("✅ API Client importado com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar API Client: {e}")

try:
    from mcp_server_one.server import mcp
    print("✅ Servidor MCP importado com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar servidor MCP: {e}")

print("🎉 Teste de importação concluído!")

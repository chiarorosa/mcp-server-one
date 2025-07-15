#!/usr/bin/env python3
"""
Script para executar o servidor MCP
"""
import sys
import os
import subprocess

def run_server():
    """Executa o servidor MCP"""
    # Adicionar o diretório src ao Python path
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    env = os.environ.copy()
    env['PYTHONPATH'] = src_path + os.pathsep + env.get('PYTHONPATH', '')
    
    # Executar o servidor
    try:
        cmd = [sys.executable, '-m', 'mcp_server_one.server'] + sys.argv[1:]
        process = subprocess.run(cmd, env=env, cwd=src_path)
        return process.returncode
    except KeyboardInterrupt:
        print("\n👋 Servidor interrompido pelo usuário")
        return 0
    except Exception as e:
        print(f"❌ Erro ao executar servidor: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_server())

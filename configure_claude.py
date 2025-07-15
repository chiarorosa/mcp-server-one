#!/usr/bin/env python3
"""
Script para configurar automaticamente o MCP Server One no Claude Desktop
"""

import json
import os
import platform
import subprocess
import sys
from pathlib import Path


def get_claude_config_path():
    """Retorna o caminho do arquivo de configuração do Claude Desktop"""
    system = platform.system()

    if system == "Windows":
        return Path(os.environ.get("APPDATA", "")) / "Claude" / "claude_desktop_config.json"
    elif system == "Darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    else:  # Linux
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"


def get_project_path():
    """Retorna o caminho absoluto do projeto"""
    return Path(__file__).parent.absolute()


def get_uv_path():
    """Retorna o caminho do executável UV"""
    try:
        result = subprocess.run(["which", "uv"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            result = subprocess.run(["where", "uv"], capture_output=True, text=True, check=True)
            return result.stdout.strip().split("\n")[0]
        except (subprocess.CalledProcessError, FileNotFoundError):
            return "uv"  # Fallback para UV no PATH


def create_mcp_config():
    """Cria a configuração do MCP Server"""
    project_path = get_project_path()

    config = {
        "mcpServers": {
            "mcp-server-one": {
                "command": "uv",
                "args": ["run", "--directory", str(project_path), "mcp-server-one"],
                "env": {},
            }
        }
    }

    return config


def update_claude_config():
    """Atualiza o arquivo de configuração do Claude Desktop"""
    config_path = get_claude_config_path()

    # Criar diretório se não existir
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Ler configuração existente ou criar nova
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                existing_config = json.load(f)
        except json.JSONDecodeError:
            existing_config = {}
    else:
        existing_config = {}

    # Adicionar ou atualizar configuração do MCP Server
    mcp_config = create_mcp_config()

    if "mcpServers" not in existing_config:
        existing_config["mcpServers"] = {}

    existing_config["mcpServers"]["mcp-server-one"] = mcp_config["mcpServers"]["mcp-server-one"]

    # Salvar configuração atualizada
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(existing_config, f, indent=2, ensure_ascii=False)

    return config_path


def main():
    """Função principal"""
    print("🚀 Configurando MCP Server One no Claude Desktop...")

    try:
        # Verificar se o projeto está configurado
        project_path = get_project_path()
        pyproject_path = project_path / "pyproject.toml"

        if not pyproject_path.exists():
            print("❌ Erro: pyproject.toml não encontrado. Execute este script do diretório do projeto.")
            sys.exit(1)

        # Verificar se UV está disponível
        uv_path = get_uv_path()
        print(f"📦 UV encontrado em: {uv_path}")

        # Atualizar configuração do Claude
        config_path = update_claude_config()
        print(f"✅ Configuração atualizada em: {config_path}")

        # Mostrar próximos passos
        print("\n🎉 Configuração concluída!")
        print("\nPróximos passos:")
        print("1. Reinicie o Claude Desktop")
        print("2. O servidor 'mcp-server-one' deve aparecer na lista de servidores MCP")
        print("3. Teste usando: uv run mcp dev src/mcp_server_one/server.py")

        # Mostrar configuração
        print(f"\n📋 Configuração adicionada:")
        mcp_config = create_mcp_config()
        print(json.dumps(mcp_config["mcpServers"]["mcp-server-one"], indent=2))

    except Exception as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

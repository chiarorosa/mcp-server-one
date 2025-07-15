# MCP Server One - Exemplo de configuração Claude Desktop

Adicione a seguinte configuração ao seu arquivo `claude_desktop_config.json`:

## Localização do arquivo de configuração:

### Windows

```
%APPDATA%\Claude\claude_desktop_config.json
```

### macOS

```
~/Library/Application Support/Claude/claude_desktop_config.json
```

### Linux

```
~/.config/Claude/claude_desktop_config.json
```

## Configuração

```json
{
  "mcpServers": {
    "mcp-server-one": {
      "command": "uv",
      "args": ["run", "mcp-server-one"],
      "env": {}
    }
  }
}
```

## Configuração com caminho absoluto (se necessário)

```json
{
  "mcpServers": {
    "mcp-server-one": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "d:\\Code\\mcp-server-one",
        "mcp-server-one"
      ],
      "env": {}
    }
  }
}
```

## Configuração com variáveis de ambiente

```json
{
  "mcpServers": {
    "mcp-server-one": {
      "command": "uv",
      "args": ["run", "mcp-server-one"],
      "env": {
        "MCP_LOG_LEVEL": "INFO",
        "MCP_SERVER_PORT": "8000"
      }
    }
  }
}
```

## Exemplo de configuração completa

```json
{
  "mcpServers": {
    "mcp-server-one": {
      "command": "uv",
      "args": ["run", "mcp-server-one", "--transport", "stdio"],
      "env": {}
    },
    "mcp-server-one-sse": {
      "command": "uv",
      "args": ["run", "mcp-server-one", "--transport", "sse", "--port", "8000"],
      "env": {}
    }
  }
}
```

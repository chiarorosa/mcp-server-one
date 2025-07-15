# Scripts de desenvolvimento

## Executar o servidor

```bash
# Usando UV
uv run python run_server.py

# Ou diretamente
uv run --directory src python -m mcp_server_one.server
```

## Testar APIs

```bash
uv run python test_apis.py
```

## Testar importações

```bash
uv run python test_import.py
```

## Executar testes

```bash
uv run pytest
```

## Formatação de código

```bash
uv run black src/ tests/
uv run isort src/ tests/
```

## Verificações

```bash
uv run mypy src/
uv run flake8 src/ tests/
```

## Instalar no Claude Desktop

```bash
# Depois de ter o servidor funcionando
uv run mcp install run_server.py --name "MCP Server One"
```

## Estrutura do projeto

```
mcp-server-one/
├── src/
│   └── mcp_server_one/
│       ├── __init__.py
│       ├── main.py          # Ponto de entrada
│       ├── server.py        # Servidor MCP principal
│       └── api_client.py    # Cliente das APIs
├── tests/
│   ├── __init__.py
│   └── test_api_client.py
├── examples/
│   └── test_client.py
├── run_server.py            # Script para executar o servidor
├── test_apis.py             # Teste das APIs
├── test_import.py           # Teste de importações
├── pyproject.toml
├── README.md
└── .gitignore
```

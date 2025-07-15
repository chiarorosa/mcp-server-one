# MCP Server One

[![GitHub](https://img.shields.io/badge/GitHub-chiarorosa%2Fmcp--server--one-blue?logo=github)](https://github.com/chiarorosa/mcp-server-one)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://python.org)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-orange.svg)](https://github.com/astral-sh/uv)

Um servidor Model Context Protocol (MCP) que fornece acesso a várias APIs públicas através de uma interface padronizada. Este servidor demonstra como integrar múltiplas APIs externas em um único servidor MCP, oferecendo recursos, ferramentas e prompts para interação com dados de diferentes fontes.

## 🚀 Características

### APIs Integradas

1. **JSONPlaceholder** - API fake para desenvolvimento e testes

   - Posts, usuários, comentários e todos
   - Operações CRUD simuladas

2. **Cat Facts API** - Fatos interessantes sobre gatos

   - Fatos aleatórios e coleções de fatos

3. **Official Joke API** - Piadas organizadas por categoria
   - Piadas aleatórias e por tipo

### Funcionalidades MCP

- **Resources**: Acesso a metadados e informações das APIs
- **Tools**: Execução de operações específicas das APIs
- **Prompts**: Templates para análise e inspiração
- **Logging**: Sistema de logs detalhado
- **Context Management**: Gerenciamento de contexto com ciclo de vida

## 📋 Requisitos

- Python 3.11+
- UV (gerenciador de pacotes Python)
- Conexão à internet para APIs externas

## 🛠️ Instalação

### Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/chiarorosa/mcp-server-one.git
cd mcp-server-one

# Instale as dependências
uv sync

# Execute o servidor
uv run mcp-server-one
```

### Instalação Detalhada

### 1. Clonar o repositório

```bash
git clone https://github.com/chiarorosa/mcp-server-one.git
cd mcp-server-one
```

### 2. Instalar dependências com UV

```bash
# Instalar dependências principais
uv sync

# Instalar dependências de desenvolvimento
uv sync --dev
```

### 3. Instalar o pacote em modo de desenvolvimento

```bash
uv pip install -e .
```

## 🎯 Uso

### Executar o servidor

#### Modo Standard I/O (padrão)

```bash
uv run mcp-server-one
# ou
uv run python -m mcp_server_one.main
```

#### Modo Server-Sent Events (SSE)

```bash
uv run mcp-server-one --transport sse --port 8000
```

#### Modo Streamable HTTP

```bash
uv run mcp-server-one --transport streamable-http --port 8000
```

#### Modo de desenvolvimento

```bash
uv run mcp dev src/mcp_server_one/server.py
```

### Testar com MCP Inspector

```bash
uv run mcp dev src/mcp_server_one/server.py
```

### Instalar no Claude Desktop

```bash
uv run mcp install src/mcp_server_one/server.py --name "MCP Server One"
```

## 📚 Recursos Disponíveis

### Resources (Recursos)

- `posts://all` - Informações sobre todos os posts
- `posts://{post_id}` - Informações sobre um post específico
- `users://all` - Informações sobre todos os usuários
- `api://status` - Status e documentação das APIs disponíveis

### Tools (Ferramentas)

#### JSONPlaceholder

- `get_posts(limit?)` - Busca posts (com limite opcional)
- `get_post_by_id(post_id)` - Busca post específico
- `get_users()` - Busca todos os usuários
- `get_user_by_id(user_id)` - Busca usuário específico
- `get_todos(user_id?)` - Busca todos (opcionalmente de um usuário)
- `create_post(title, body, user_id)` - Cria post (simulado)

#### Cat Facts

- `get_cat_fact()` - Fato aleatório sobre gatos
- `get_multiple_cat_facts(limit=5)` - Múltiplos fatos sobre gatos

#### Jokes

- `get_random_joke()` - Piada aleatória
- `get_jokes_by_type(type)` - Piadas por tipo (programming, general, etc.)

### Prompts (Templates)

- `analyze_post(post_id)` - Análise detalhada de um post
- `user_profile_analysis(user_id)` - Análise de perfil de usuário
- `daily_inspiration()` - Mensagem de inspiração diária

## 🔧 Configuração

### Variáveis de ambiente

O servidor não requer configuração específica, mas você pode personalizar:

```bash
export MCP_SERVER_PORT=8000
export MCP_LOG_LEVEL=INFO
```

### Configuração do Claude Desktop

Adicione ao seu `claude_desktop_config.json`:

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

## 🧪 Testes

### Executar testes

```bash
# Todos os testes
uv run pytest

# Testes com cobertura
uv run pytest --cov=mcp_server_one

# Testes específicos
uv run pytest tests/test_api_client.py

# Testes em modo verbose
uv run pytest -v
```

### Testes de integração

```bash
# Testar APIs reais (requer internet)
uv run pytest tests/test_integration.py
```

## 📊 Desenvolvimento

### Estrutura do projeto

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
│   └── test_api_client.py   # Testes unitários
├── pyproject.toml           # Configuração do projeto
└── README.md
```

### Linting e formatação

```bash
# Formatação com black
uv run black src/ tests/

# Ordenação de imports
uv run isort src/ tests/

# Verificação de tipos
uv run mypy src/

# Linting
uv run flake8 src/ tests/
```

### Adicionar nova API

1. Adicione a classe da API em `api_client.py`
2. Registre no `APIManager`
3. Adicione tools no `server.py`
4. Adicione testes em `test_api_client.py`

## 🔍 Exemplos de Uso

### 1. Buscar posts

```python
# Através do cliente MCP
result = await session.call_tool("get_posts", {"limit": 5})
```

### 2. Análise de usuário

```python
# Usar o prompt de análise
prompt = await session.get_prompt("user_profile_analysis", {"user_id": 1})
```

### 3. Inspiração diária

```python
# Usar o prompt de inspiração
prompt = await session.get_prompt("daily_inspiration", {})
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

### Diretrizes de contribuição

- Mantenha o código limpo e bem documentado
- Adicione testes para novas funcionalidades
- Siga o estilo de código existente
- Atualize a documentação quando necessário

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## 🆘 Suporte

### Problemas comuns

1. **Erro de importação do MCP**: Certifique-se de que o pacote `mcp` está instalado
2. **APIs não respondem**: Verifique sua conexão com a internet
3. **Porta em uso**: Mude a porta com `--port`

### Logs e debugging

```bash
# Modo verbose
uv run mcp-server-one --verbose

# Logs detalhados
uv run mcp dev src/mcp_server_one/server.py --log-level DEBUG
```

### Contato

- Issues: [GitHub Issues](https://github.com/chiarorosa/mcp-server-one/issues)
- Discussões: [GitHub Discussions](https://github.com/chiarorosa/mcp-server-one/discussions)

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir.

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🎉 Agradecimentos

- [Model Context Protocol](https://modelcontextprotocol.io/) pela especificação
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) pela API de teste
- [Cat Facts API](https://catfact.ninja/) pelos fatos interessantes
- [Official Joke API](https://official-joke-api.appspot.com/) pelas piadas

---

**Feito com ❤️ usando Model Context Protocol e UV**

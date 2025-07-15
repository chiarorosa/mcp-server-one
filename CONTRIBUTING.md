# Contribuindo para o MCP Server One

Obrigado por considerar contribuir para o MCP Server One! 🎉

## Como Contribuir

### Relatando Bugs

Se você encontrar um bug, por favor abra uma [issue](https://github.com/chiarorosa/mcp-server-one/issues) incluindo:

- Descrição detalhada do problema
- Passos para reproduzir
- Comportamento esperado vs. atual
- Versão do Python e sistema operacional
- Logs de erro (se disponíveis)

### Sugerindo Melhorias

Para sugerir melhorias:

1. Abra uma [issue](https://github.com/chiarorosa/mcp-server-one/issues) com a tag "enhancement"
2. Descreva detalhadamente sua sugestão
3. Explique por que seria útil para o projeto

### Desenvolvendo

#### Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/chiarorosa/mcp-server-one.git
cd mcp-server-one

# Instale dependências de desenvolvimento
uv sync --dev

# Execute os testes
uv run pytest

# Execute o linter
uv run flake8 src/

# Execute o formatador
uv run black src/
```

#### Processo de Contribuição

1. **Fork** o projeto
2. **Crie uma branch** para sua feature:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Faça suas mudanças** seguindo as diretrizes abaixo
4. **Adicione testes** para suas mudanças
5. **Execute os testes** para garantir que tudo funciona
6. **Commit suas mudanças**:
   ```bash
   git commit -m "feat: add amazing feature"
   ```
7. **Push para sua branch**:
   ```bash
   git push origin feature/amazing-feature
   ```
8. **Abra um Pull Request**

#### Diretrizes de Código

- Siga o estilo PEP 8 para Python
- Use type hints quando possível
- Documente funções e classes importantes
- Mantenha funções pequenas e focadas
- Adicione testes para novas funcionalidades

#### Mensagens de Commit

Use o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` para novas funcionalidades
- `fix:` para correções de bugs
- `docs:` para mudanças na documentação
- `style:` para formatação e estilo
- `refactor:` para refatorações
- `test:` para adição de testes
- `chore:` para tarefas de manutenção

### Adicionando Novas APIs

Para adicionar uma nova API:

1. Crie uma nova classe em `src/mcp_server_one/api_client.py`
2. Implemente os métodos necessários
3. Adicione as ferramentas MCP correspondentes em `src/mcp_server_one/server.py`
4. Adicione testes em `tests/test_api_client.py`
5. Atualize a documentação no README.md

### Testando

```bash
# Executar todos os testes
uv run pytest

# Executar testes específicos
uv run pytest tests/test_api_client.py

# Executar com cobertura
uv run pytest --cov=src/mcp_server_one

# Testar manualmente
uv run python test_apis.py
```

### Documentação

- Mantenha o README.md atualizado
- Documente novas APIs e ferramentas
- Atualize exemplos quando necessário
- Use comentários claros no código

## Diretrizes da Comunidade

- Seja respeitoso e inclusivo
- Ajude outros desenvolvedores
- Mantenha discussões construtivas
- Reporte comportamentos inadequados

## Perguntas?

Se você tiver dúvidas sobre como contribuir:

- Abra uma [issue](https://github.com/chiarorosa/mcp-server-one/issues) com a tag "question"
- Inicie uma [discussão](https://github.com/chiarorosa/mcp-server-one/discussions)

Obrigado pela sua contribuição! 🚀

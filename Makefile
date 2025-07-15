# Makefile para MCP Server One

.PHONY: help install test format lint run clean

help:
	@echo "Comandos disponíveis:"
	@echo "  install    - Instala dependências"
	@echo "  test       - Executa testes"
	@echo "  test-apis  - Testa conectividade com APIs"
	@echo "  format     - Formata código"
	@echo "  lint       - Executa linting"
	@echo "  run        - Executa servidor"
	@echo "  clean      - Limpa arquivos temporários"

install:
	uv sync

test:
	uv run pytest

test-apis:
	uv run python test_apis.py

format:
	uv run black src/ tests/
	uv run isort src/ tests/

lint:
	uv run mypy src/
	uv run flake8 src/ tests/

run:
	uv run python run_server.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

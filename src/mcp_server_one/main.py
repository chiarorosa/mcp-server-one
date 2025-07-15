"""
Ponto de entrada principal do MCP Server One
"""
import click
from .server import main as server_main


@click.command()
@click.option(
    "--transport",
    default="stdio",
    type=click.Choice(["stdio", "sse", "streamable-http"]),
    help="Tipo de transporte para usar (stdio, sse, streamable-http)"
)
@click.option(
    "--port",
    default=8000,
    type=int,
    help="Porta para usar com transporte sse ou streamable-http"
)
@click.option(
    "--host",
    default="localhost",
    help="Host para usar com transporte sse ou streamable-http"
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Habilita logs verbosos"
)
def main(transport: str, port: int, host: str, verbose: bool):
    """
    MCP Server One - Servidor MCP com APIs públicas
    
    Este servidor fornece acesso a várias APIs públicas através do
    Model Context Protocol (MCP).
    """
    import sys
    
    # Configurar argumentos para o servidor
    sys.argv = ["mcp-server-one"]
    
    if transport != "stdio":
        sys.argv.extend(["--transport", transport])
        if transport in ["sse", "streamable-http"]:
            sys.argv.extend(["--port", str(port)])
            sys.argv.extend(["--host", host])
    
    if verbose:
        sys.argv.append("--verbose")
    
    # Executar o servidor
    server_main()


if __name__ == "__main__":
    main()

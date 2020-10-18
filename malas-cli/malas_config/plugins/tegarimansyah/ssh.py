import click
from malas_core.run import bash
from .server import get_server

@click.command()
def command():
    """Connect to server via ssh"""
    server = get_server()
    bash('ssh -i {ssh_key_path} {username}@{hostname}'.format(
        ssh_key_path=server.get('ssh_key_path'),
        username=server.get('username'),
        hostname=server.get('hostname')
    ))
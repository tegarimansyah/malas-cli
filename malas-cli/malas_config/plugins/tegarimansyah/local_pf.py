import click
from malas_core.run import bash
from .server import get_server, get_port

@click.command()
def command():
    """Port forwarding from server to local"""
    server = get_server()
    port = get_port()
    
    click.echo(f'{server.get("hostname")}:{port} -> localhost:{port}')
    click.echo('CTRL+C for quit')
    bash('ssh -N -L {port}:localhost:{port} -i {ssh_key_path} {username}@{hostname}'.format(
        ssh_key_path=server.get('ssh_key_path'),
        username=server.get('username'),
        hostname=server.get('hostname'),
        port=port
    ))
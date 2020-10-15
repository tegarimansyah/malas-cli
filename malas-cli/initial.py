import os
import click

from helper import config_path

@click.command()
def initial():
    """
    Initialize folder and other
    """
    
    folders = ['templates', 'plugins']
    for folder in folders:
        os.makedirs(f'{config_path}/{folder}', exist_ok=True)

    click.echo(f"Creating configuration folder in {config_path}")
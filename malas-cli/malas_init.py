import os
import click

from distutils.dir_util import copy_tree
from malas_path import config_path

@click.command()
def initial():
    """
    Initialize folder and other
    """
        
    folders = ['config', 'plugins']
    for folder in folders:
        os.makedirs(f'{config_path}/{folder}', exist_ok=True)


    copy_tree(src=os.path.dirname(__file__) + '/malas_config/', dst=config_path)

    click.echo(f"Creating configuration folder in {config_path}")
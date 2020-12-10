import os
import click
from PyInquirer import prompt

from distutils.dir_util import copy_tree, remove_tree
from malas_path import config_path, malas_path

questions = [
    # Learn more in https://github.com/CITGuru/PyInquirer#question-types
    {
        'type': 'confirm',
        'name': 'confirmation',
        'message': 'Configuration already exist, reset to factory?',
        'default': True
    },
    {
        'type': 'confirm',
        'name': 'keep_config',
        'message': 'Keep config?',
        'default': True
    },

]

@click.command()
def initial():
    """
    Initialize folder and other
    """
    replace = True
    keep_config = False

    if os.path.isdir(config_path):
        answer = prompt(questions)
        replace = answer.get('confirmation')
        keep_config = answer.get('keep_config')

    if replace:
        if os.path.isdir(f'{config_path}/config'):
            copy_tree(src=f'{config_path}/config', dst=f'{config_path}/config_backup')
            remove_tree(f'{config_path}/config')

        folders = ['config', 'plugins']
        for folder in folders:
            os.makedirs(f'{config_path}/{folder}', exist_ok=True)

        copy_tree(src=f'{malas_path}/malas_config/', dst=config_path)

        if keep_config:
            copy_tree(src=f'{config_path}/config_backup', dst=f'{config_path}/config')
            remove_tree(f'{config_path}/config_backup')

        click.echo(f"Creating configuration folder in {config_path}")
    else:
        click.echo("Nothing change")

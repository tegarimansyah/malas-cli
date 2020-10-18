import click

from PyInquirer import prompt
from malas_core.run import bash
from .server import get_server

questions = [
    {
        'type': 'input',
        'name': 'tag',
        'message': 'Your docker tag',
    },
    {
        'type': 'input',
        'name': 'dockerfile',
        'message': 'Your dockerfile',
        'default': 'Dockerfile'
    },
    {
        'type': 'input',
        'name': 'context',
        'message': 'Your context',
        'default': '.'
    },
]

@click.command()
def command():
    """Build docker in remote server"""
    server = get_server()
    answers = prompt(questions)

    bash('ssh-add {ssh_key_path} && DOCKER_HOST=ssh://{username}@{hostname} docker buildx build -t {tag} -f {dockerfile} {context}'.format(
        ssh_key_path=server.get('ssh_key_path'),
        username=server.get('username'),
        hostname=server.get('hostname'),
        tag=answers.get('tag'),
        dockerfile=answers.get('dockerfile'),
        context=answers.get('context')
    ))
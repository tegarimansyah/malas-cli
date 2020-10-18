import os
import click
import json

from PyInquirer import prompt
from malas_path import home_path, config_path

ssh_list = os.listdir(f'{home_path}/.ssh')

questions = [
    # Learn more in https://github.com/CITGuru/PyInquirer#question-types
    {
        'type': 'input',
        'name': 'server_name',
        'message': 'Server Name',
    },
    {
        'type': 'input',
        'name': 'hostname',
        'message': 'Hostname or IP address',
    },
    {
        'type': 'input',
        'name': 'username',
        'message': 'Username',
    },
    {
        'type': 'list',
        'name': 'ssh_key_path',
        'message': 'SSH Key Path',
        'choices': ssh_list
    },
]

@click.command()
def command():
    """Create Server Shortcut"""
    answers = prompt(questions)
    if answers:
        server_file = f'{config_path}/config/server.json'
        answers['ssh_key_path'] = f'{home_path}/.ssh/{answers.get("ssh_key_path")}'

        with open(server_file, 'r+') as jsonfile:
            server_list = json.load(jsonfile)
            server_list.append(answers)
            jsonfile.seek(0)
            json.dump(server_list, jsonfile, indent=4)
            jsonfile.truncate()

        click.echo(f'Server {answers.get("serve_name")} saved')

def get_server():
    server_file = f'{config_path}/config/server.json'

    with open(server_file, 'r') as jsonfile:
        server_data = json.load(jsonfile)
        server_list = [server_list['server_name'] for server_list in server_data]
        if server_list:
            questions = [{
                'type': 'list',
                'name': 'server_name',
                'message': 'Choose Server',
                'choices': server_list
            }]
            answer = prompt(questions)
            server_name = answer.get('server_name')
            return [server for server in server_data if server['server_name'] == server_name][0]
        else:
            click.echo("Server is empty")
        
import os
import click
from PyInquirer import prompt

from malas_core.run import bash_script
from .server import get_server

questions = [
    # Learn more in https://github.com/CITGuru/PyInquirer#question-types
    {
        'type': 'rawlist',
        'name': 'filename',
        'message': 'Select file (Showing top 8 files)',
        'choices': ['I will write my self'] + [filename for filename in os.listdir() if '.sh' in filename][:8]
    },
    {
        'type': 'input',
        'name': 'params',
        'message': 'Write params or filename'
    }
]

@click.command()
def command():
    """Run bash script in server"""
    server = get_server()
    
    answers = prompt(questions)
    filename = answers.get('filename')
    params = answers.get('params')

    if filename == 'I will write my self':
        filename = params.split(' ')[0]
        params = ' '.join(params.split(' ')[1:])

    bash_script(filename, params=params, remote=server)
    
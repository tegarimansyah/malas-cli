import click
from PyInquirer import prompt

questions = [
    # Learn more in https://github.com/CITGuru/PyInquirer#question-types
    {
        'type': 'input',
        'name': 'name',
        'message': 'Your name?',
    }
]

@click.command()
def command():
    """Do some greeting"""

    answers = prompt(questions)
    if answers:
        name = answers.get("name")
        click.echo(f"Welcome to the lazy world, {name}")
# List of all command
import click

@click.group()
def install():
    """Install app and configure it"""
    pass

@click.group()
def setup():
    """Setup app and configure it"""
    pass

@click.group()
def publish():
    """Publish app"""
    pass

@click.group()
def do_something():
    """Do something awesome"""
    pass

command_func_list = {
    'setup': setup,
    'install': install,
    'publish': publish,
    'do': do_something,
    # Add more here after create function like above
}
        
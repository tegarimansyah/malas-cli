import click
import helper
from initial import initial

@click.group()
def main():
    """
    I'm too lazy to type commands to do boring devops stuff.
    So I create this CLI tools.
    """
    pass

main.add_command(initial, name="init")

if __name__ == "__main__":
    try:
    # Check plugins
        from malas_plugins import (
            install,
            setup,
            publish,
            do_something
        )
        
        main.add_command(install, name="install")
        main.add_command(setup, name="setup")
        
        main()
    
    except ImportError:
        click.echo("Do `malas init` for initialize")

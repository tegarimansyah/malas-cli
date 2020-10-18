import click
import importlib
import malas_path
from malas_init import initial

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
        import command_aggregate
        from command_func import command_func_list
        for module_name, module_func in command_func_list.items():
            main.add_command(module_func, name=module_name)

        main()
        
    except ImportError as e:

        click.echo("-------ERROR------")
        click.echo(e)
        click.echo("If this is your first attempt, please do 'malas init'")
        click.echo("-------ERROR------")

        main()
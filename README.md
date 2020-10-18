# malas-cli

A collection of automating boring stuff for devops in single command line.

Dependency:

* click
* PyInquirer
* cookiecutter

## Install

Sorry, the package is not ready yet. But you can do this:

* Clone this repo
* Create env variable and run `pip install -r requirements.txt`
* Add alias in `.bashrc` or `.zshrc` or equivalent
* Restart terminal

sample alias

```bash
# Fomat
alias malas="/path/to/python /path/to/malas.py"

# Example, python run using virtualenvwrapper
alias malas="/home/tegar/.virtualenvs/project_malas/bin/python /home/tegar/malas-cli/malas-cli/malas.py"
```

## Testing

* First thing first, populate config. It will create `$HOME/.malas` folder.

```
$ malas init
Creating configuration folder in /home/tegar/.malas

$ malas
Usage: malas.py [OPTIONS] COMMAND [ARGS]...

  I'm too lazy to type commands to do boring devops
  stuff. So I create this CLI tools.

Options:
  --help  Show this message and exit.

Commands:
  do       Do something awesome
  init     Initialize folder and other
  install  Install app and configure it
  publish  Publish app
  setup    Setup app and configure it

$ malas setup
Usage: malas.py setup [OPTIONS] COMMAND [ARGS]...

  Setup app and configure it

Options:
  --help  Show this message and exit.

Commands:
  server          Create Server Shortcut
  ssh_connection  Connect to server via ssh
```

* From example above, if we run `malas setup server`, a prompt will appear

## How it works?

Let's see configuration folder

```
$ tree ~/.malas 

/home/tegar/.malas
├── command_aggregate.py
├── command_func.py
├── config
│   └── server.json
├── plugins
│   └── tegarimansyah
│       ├── hello_world.py
│       ├── server.py
│       └── ssh.py
└── sub_command.py
```

We can put automation script in plugins folder, namespacing with your own namespace. In the future, I hope we will able to pull from github repository and namespacing based on username.

Let's see our `plugins/tegarimansyah/hello_world.py`

```python
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
```

**Malas** will **only** call `command` function, you can call other function from that. The `command` function must decorated using `@click.command()`. The rest is not mandatory.

After putting your automation script, then we can register it in `sub_command.py`.

```python
# List of all sub command
sub_command_list = {
    "install": [
    ],
    "setup": [
        { "sub_command":"server", "module":"tegarimansyah.server" },
        { "sub_command":"ssh_connection", "module":"tegarimansyah.ssh" },
    ],
    "publish": [
    ],
    "do": [
        { "sub_command":"hello_world", "module":"tegarimansyah.hello_world" },
    ],
}
```

We can see, `server` and `ssh` file is under `setup` command, `hello_world` file in under `do` command. But let see for `ssh`, we can run it using `malas setup ssh_connection`, **not** `malas setup ssh`. You may want to `distinguish` subcommand and file name.

But how if I want to add more command? Let's see `command_func.py`

```python
...

@click.group()
def install():
    """Install app and configure it"""
    pass

...

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
```

You can create your own command function with decorator `@click.group()` then register it in `command_func_list`.

After all of it, `command_aggregate.py` will do some importing magic. Don't need to restart, just run `malas your_new_command your_new_subcommand`. It will lazily (*malas*) run your script.

---

# Example Command (That I dream, not implemented yet)

For now, the script will only run on Ubuntu and derivative

## Malas Install

```bash
$ malas install docker # will install docker, docker compose and set to current user
$ malas install nginx # will instal 
```

## Malas Set Up

```bash
$ malas setup nginx # Generate config and apply it
$ malas setup cloudflare # Create new dns record for your cloudflare
$ malas setup wireguard # Create new user for your wireguard config
$ malas setup ssh # Create ssh keygen then transfer to server or copy to clipboard
$ malas setup kubernetes # Create deployment or config
```

## Malas Build 

```bash
$ malas build docker # Connect to docker (or remote server), build, tagging and push to registry
```

## Malas Publish

```bash
$ malas publish docker-compose # Run green-blue docker compose
$ malas publish django # Pull from github, migrate, collectstatic then restart systemd
```


## Malas Login

If you are really lazy to remind everything (IP, domain, etc), just centralize it. 

```bash
$ malas register
$ malas login
```

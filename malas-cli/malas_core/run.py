import os
import subprocess

def bash(command):
    subprocess.call(command, shell=True)

def bash_script(filename, params='', remote=''):
    # execute local script on remote
    # https://unix.stackexchange.com/questions/87405/how-can-i-execute-local-script-on-remote-machine-and-include-arguments
    # ssh serverA "bash -s" -- < ./ex.bash "-time" "bye"

    if remote == '':
        command = f"bash {filename} {params}"
    else:
        command = 'ssh -i {ssh_key_path} {username}@{hostname} "bash -s" -- < {filename} {params}'.format(
            ssh_key_path=remote.get('ssh_key_path'),
            username=remote.get('username'),
            hostname=remote.get('hostname'),
            filename=f'{os.getcwd()}/{filename}',
            params=params
        )

    subprocess.call(command, shell=True)

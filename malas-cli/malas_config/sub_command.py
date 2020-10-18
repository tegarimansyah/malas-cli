# List of all sub command
sub_command_list = {
    "install": [
    ],
    "setup": [
        { "sub_command":"server", "module":"tegarimansyah.server" },
        { "sub_command":"ssh-connection", "module":"tegarimansyah.ssh" },
        { "sub_command":"local-pf", "module":"tegarimansyah.local_pf" },
    ],
    "publish": [
    ],
    "do": [
        { "sub_command":"hello-world", "module":"tegarimansyah.hello_world" },
    ],
}
        
# Import all plugins and config
import os
import importlib
from command_func import command_func_list
from sub_command import sub_command_list

plugin_dir = os.path.dirname(__file__)

for command in sub_command_list.keys():
    for module_object in sub_command_list.get(command):
        module = importlib.import_module('plugins.' + module_object.get('module'))
        if 'command' in dir(module):
            command_func = command_func_list.get(command)
            command_func.add_command(module.command, name=module_object.get("sub_command"))
        else:
            raise ImportError(f"{module} doesn't have 'command' method. Please follow the malas structure.")
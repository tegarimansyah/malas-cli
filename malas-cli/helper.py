import sys
from pathlib import Path

home_path = str(Path.home())
config_path = f'{home_path}/.malas'

sys.path.insert(1, config_path)

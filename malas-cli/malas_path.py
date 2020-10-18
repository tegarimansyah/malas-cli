import os, sys
from pathlib import Path

home_path = str(Path.home())
config_path = f'{home_path}/.malas'
malas_path = os.path.dirname(__file__)
sys.path.insert(1, config_path)

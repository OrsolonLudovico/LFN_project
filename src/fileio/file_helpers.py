import os
import yaml

def get_file_path(filename, folder):
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "..", "..", folder, filename)

def read_config_file():
    path = get_file_path('config.yaml', 'config')
    with open(path, 'r') as file:
        return yaml.safe_load(file)
import os
import yaml

def get_file_path(filename, folder):
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "..", folder, filename)
    folder_path = os.path.dirname(file_path)  # Get the folder without the file name
    # Create folder if it doesn't exist (use exist_ok=True to avoid race conditions)
    os.makedirs(folder_path, exist_ok=True)

    #return os.path.join(script_dir, "..", "..", folder, filename)
    return os.path.normpath(file_path)  # Normalize the path

def read_config_file():
    path = get_file_path('config.yaml', 'config')
    with open(path, 'r') as file:
        return yaml.safe_load(file)
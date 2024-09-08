import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)]: %(mesasage)s')

project_name = 'TextSummary'

list_files = [
    '.github/workflows/.gitkeep', #ci/cd workflow for building the project
    f'src/{project_name}/__init__.py', #init file or constructor file for the project, so the project become a package can be imported
    f'src/{project_name}/components/__init__.py', 
    f'src/{project_name}/utils/__init__.py', 
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/loggging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/config.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/t.ipynb' #contains notebooks data and experiments
]

for file_path in list_files:
    file_path = Path(file_path) # convert Path to be alighned with the current os
    file_dir, _ = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True) #if the folder exists already it will not raise an error
    if (not os.path.exists(file_path)):
        with open(file_path, 'w') as f:
            pass  # create an empty file if it does not exist already

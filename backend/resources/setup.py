import json
import subprocess

with open('backend/resources/requirements.json', 'r') as file:
    dependencies = json.load(file)

for package, version in dependencies.items():
    subprocess.run(['pip', 'install', f'{package}=={version}'])
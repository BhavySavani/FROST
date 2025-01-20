import os
import shutil
import json

def create_project_structure(config_file, parent_dir):
  
    with open(config_file, 'r') as file:
        config = json.load(file)

    protocols = set(sensor['protocol'] for sensor in config.get('devices', []))

    project_dir = config["project_name"]
    for protocol in protocols:
        protocol_folder = os.path.join(parent_dir, protocol.lower())
        target_folder = os.path.join(project_dir, protocol.lower())

        if os.path.exists(protocol_folder):
            if not os.path.exists(target_folder):
                shutil.copytree(protocol_folder, target_folder)
        else:
            print(f"Warning: Folder for protocol '{protocol}' does not exist in parent directory.")

    print(f"Project structure created at: {project_dir}")

create_project_structure('main/devices_config.json', 'main/core_ips')

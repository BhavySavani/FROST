import argparse
import logging
import os 

from fpga.project import Project

logging.basicConfig()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--action', choices=['generate', 'transfer', 'all'], default='generate',
)
args = parser.parse_args()

# Function to add all files from a directory to the project
def add_files_from_directory(prj, directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.v'):  # Only add Verilog files
                prj.add_files(os.path.join(root, file))
                print(os.path.join(root,file))


prj = Project("libero")
prj.set_part('m2s010-1-tq144')

# Add all Verilog files from the output project folder
output_project_folder = '../../output_project'
add_files_from_directory(prj, output_project_folder)
prj.add_files('../../output_project/mkr.pdc')
prj.add_files('../../output_project/mkr.sdc')
prj.set_top('../../output_project/top_module.v')


if args.action in ['generate', 'all']:
    try:
        prj.generate()
    except RuntimeError:
        print('ERROR:generate:Libero not found')

if args.action in ['transfer', 'all']:
    print('ERROR:transfer:Not yet implemented')

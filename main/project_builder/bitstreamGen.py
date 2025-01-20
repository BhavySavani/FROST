import argparse
import logging
import os
import sys
from fpga.project import Project

logging.basicConfig()

filtered_args = [arg for arg in sys.argv if arg.startswith("--")]

project_directory = sys.argv[1]
parser = argparse.ArgumentParser()
parser.add_argument(
    '--action', choices=['generate', 'transfer', 'all'], default='generate',
)
args = parser.parse_args(filtered_args)

def add_files_from_directory(prj, directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.v'):  
                prj.add_files(os.path.join(root, file))
                print(os.path.join(root, file))


prj = Project("libero")
prj.set_part('m2s010-1-tq144')

output_project_folder = f'../../{project_directory}'
add_files_from_directory(prj, output_project_folder)
prj.add_files(output_project_folder + '/mkr.pdc')
prj.add_files(output_project_folder + '/mkr.sdc')
prj.set_top(output_project_folder + '/top_module.v')

if args.action in ['generate', 'all']:
    try:
        prj.generate()
    except RuntimeError:
        print('ERROR:generate:Libero not found')

if args.action in ['transfer', 'all']:
    print('ERROR:transfer:Not yet implemented')

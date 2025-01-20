import argparse
import os
import subprocess

def execute_python_files(target_directory, project_directory, execution_order):
    """
    Executes Python files in the specified order, passing the project_directory as an argument.
    """
    for py_file in execution_order:
        py_file_path = os.path.join(target_directory, py_file)
        if not os.path.exists(py_file_path):
            print(f"Error: File '{py_file}' does not exist in {target_directory}.")
            return
        print(f"Executing {py_file} with project_directory = {project_directory}")
        
        # Execute the Python file with subprocess, passing the project_directory as an argument
        result = subprocess.run(['python', py_file_path, project_directory], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error executing {py_file}: {result.stderr}")
            return
        
        print(f"Output of {py_file}:\n{result.stdout}")

def main():
    parser = argparse.ArgumentParser(description="Manage project creation and execute scripts.")
    parser.add_argument(
        'project_directory',
        type=str,
        help='The folder name of the second folder (config folder).'
    )
    parser.add_argument(
        '-c',
        '--command',
        type=str,
        choices=['create-project'],
        required=True,
        help='Command to execute. Currently supports "create-project".'
    )
    
    args = parser.parse_args()
    
    # Define the folder structure
    main_directory = "main/"
    scripts_folder = os.path.join(main_directory, "project_builder")  # Replace with your scripts folder name
    config_folder = args.project_directory
    
    # Check if project_directory exists
    if not os.path.exists(config_folder):
        print(f"Error: The project_directory '{args.project_directory}' does not exist.")
        return
    
    # Define the order of execution
    execution_order = [
        "add_verilog_to_project.py",  # First script
        "verilogGen.py",  # Second script
        "sdc_pdc_gen.py",  # Third script
        "bitstreamGen.py"   # Fourth script
    ]
    
    # Check and execute the command
    if args.command == 'create-project':
        execute_python_files(scripts_folder, args.project_directory, execution_order)

if __name__ == "__main__":
    main()

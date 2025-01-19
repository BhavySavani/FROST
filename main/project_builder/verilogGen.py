import json
import os
import sys
def read_json(file_path):
    """
    Reads a JSON file and returns its contents as a dictionary.
    """
    with open(file_path, "r") as file:
        return json.load(file)

def generate_verilog_top(device_config_path, protocol_config_path, output_file="top_module.v"):
    """
    Generates a Verilog top module file based on device and protocol configuration.
    """
    # Read configurations
    device_config = read_json(device_config_path)
    protocol_config = read_json(protocol_config_path)
    
    # Extract clock and devices
    clk = device_config["clk"]
    devices = device_config["devices"]
    protocols = {p["protocol"]: p for p in protocol_config["protocols"]}
    
    # Start building the Verilog file
    verilog_code = f"module top_module (\n"
    
    # Add inputs and outputs for clock and devices
    all_inputs = []
    all_outputs = []
    
    for device in devices:
        name = device["name"]
        protocol = device["protocol"]
        protocol_details = protocols.get(protocol)

        if not protocol_details:
            raise ValueError(f"Protocol {protocol} not defined in protocol configuration.")

        # Inputs and outputs for the device
        inputs = protocol_details["inputs"]
        outputs = protocol_details["outputs"]
        
        for inp in inputs:
            all_inputs.append(f"input wire {name}_{protocol}_{inp}")
        for out in outputs:
            all_outputs.append(f"output wire {name}_{protocol}_{out}")
    
    # Add inputs and outputs to the top module
    verilog_code += ",\n".join(all_inputs + all_outputs) + "\n);\n\n"
    
    # Instantiate devices
    for device in devices:
        name = device["name"]
        protocol = device["protocol"]
        protocol_details = protocols.get(protocol)

        if not protocol_details:
            raise ValueError(f"Protocol {protocol} not defined in protocol configuration.")

        # Inputs and outputs for the device
        inputs = protocol_details["inputs"]
        outputs = protocol_details["outputs"]
        parameters = protocol_details["parameters"]

        # device's ports
        device_ports = []
        for inp in inputs:
            device_ports.append(f"    .{inp}({name}_{protocol}_{inp})")
        for out in outputs:
            device_ports.append(f"    .{out}({name}_{protocol}_{out})")
        
        # Parameters (only add if there are any)
        device_params = []
        if parameters:  # Check if parameters exist
            for param in parameters:
                if param in device:
                    device_params.append(f"    .{param}({device[param]})")
                elif param == "clk_frequency":
                    device_params.append(f"    .{param}({clk})")  # Use the global clock for clk_frequency
            
            # Add the parameters to the instantiation
            verilog_code += f"    {protocol} {name}_{protocol}#(\n"
            verilog_code += ",\n".join(device_params)
            verilog_code += "\n) (\n"
        else:
            # If no parameters, skip the #() part
            verilog_code += f"    {protocol} {name}_{protocol} (\n"
        
        # Add the ports for the device
        verilog_code += ",\n".join(device_ports)
        verilog_code += "\n    );\n\n"

    # End module
    verilog_code += "endmodule"

    # Write to file
    with open(output_file, "w") as file:
        file.write(verilog_code)

    print(f"Verilog top module generated: {output_file}")

# Paths to JSON files
device_config_path = "..\devices_config.json"
protocol_config_path = "..\protocol_config.json"
# Generate the Verilog file
generate_verilog_top(device_config_path, protocol_config_path)

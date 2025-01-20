import json

def create_config(fpga_details):
    device_dict = {}
    device_dict["fpga"] = fpga_details[0]
    device_dict["frequency"] = fpga_details[1]
    device_dict["project_type"] = fpga_details[2]
    device_dict["sensors"] = []
    with open("main/devices_config.json","w") as f:
        json.dump(device_dict,f)   

def add_sensors(sensors):
    with open("main/devices_config.json","r") as f:
        device_dict = json.load(f)
    with open("main/protocol_config.json",'r') as f:
        protocols = json.load(f)
    parameter_list = []
    for i in protocols["protocols"]:
        if i["protocol"] == sensors[1]:
            parameter_list = i["parameters"]
    
    sensor_dict = {}
    sensor_dict["name"] = sensors[0]
    sensor_dict["protocols"] = sensors[1]

    print("parameter list ",parameter_list)
    for i in range(len(sensors)):
        if i>=2:
            print(parameter_list[0])
            sensor_dict[parameter_list[0]] = sensors[i]
            parameter_list.pop()

    device_dict["sensors"].append(sensor_dict)

    with open("main/devices_config.json","w") as f:
        json.dump(device_dict,f)   


def project_name_gen(project_name):
    with open("main/devices_config.json","r") as f:
        device_dict = json.load(f)
        
    device_dict["project_name"] = project_name
    
    with open("main/devices_config.json","w") as f:
        json.dump(device_dict,f)
    
    
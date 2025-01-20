import json
import os

def create_config(fpga_details):
    
    with open("main/tempfile.json","r") as f:
        device_dict = json.load(f)
    project_name = device_dict["project_name"]
    device_dict["fpga"] = fpga_details[0]
    device_dict["frequency"] = int(fpga_details[1])
    device_dict["project_type"] = fpga_details[2]
    device_dict["sensors"] = []
    with open(f"{project_name}/devices_config.json","w") as f:
        json.dump(device_dict,f)   

def add_sensors(sensors):
    with open("main/tempfile.json","r") as f:
        project_name = json.load(f)
    with open(f"{project_name["project_name"]}/devices_config.json","r") as f:
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
    print("sensors",sensors)
    for i in range(len(sensors)):
        if i>=2:
            if 'M' in sensors[i]:
                sensors[i]=sensors[i].replace('M','')
                print(sensors[i])
                sensors[i]=int(sensors[i])*(10E6)
                sensor_dict[parameter_list[0]] = sensors[i]
                parameter_list.pop()
            elif 'K' in sensors[i]:
                sensors[i]=sensors[i].replace('K','')
                sensors[i]=int(sensors[i])*(10E3)
                sensor_dict[parameter_list[0]] = sensors[i]
                parameter_list.pop()
            else:
                print(parameter_list[0])
                sensor_dict[parameter_list[0]] = sensors[i]
                parameter_list.pop()

    device_dict["sensors"].append(sensor_dict)

    with open(f"{project_name["project_name"]}/devices_config.json","w") as f:
        json.dump(device_dict,f)   


def project_name_gen(project_name):
    os.makedirs(project_name, exist_ok=True)
    device_dict = {"project_name":project_name}

    with open(f"{project_name}/devices_config.json","w") as f:
        json.dump(device_dict,f)
    with open(f"main/tempfile.json","w") as f:
        json.dump(device_dict,f)
    
def delete_tempfile():
    os.remove("main/tempfile.json")

    
import json

def create_config(fpga_details):
    device_dict = {}
    device_dict["fpga"] = fpga_details[0]
    device_dict["frequency"] = fpga_details[1]
    device_dict["project_type"] = fpga_details[2]
    device_dict["sensors"] = []
    return device_dict

def add_sensors(sensors,device_dict):
    f = open("protocol_config.json",'r')
    protocols = json.load(f)
    parameter_list = []
    for i in protocols["protocols"]:
        if i["protocol"] == sensors[1]:
            parameter_list = i["parameters"]
    
    sensor_dict = {}
    sensor_dict["name"] = sensors[0]
    sensor_dict["protocols"] = sensors[1]

    for i in range (len(parameter_list)):
        sensor_dict[parameter_list[i]] = sensors[i+2]

    device_dict["sensors"].append(sensor_dict)

    return device_dict        

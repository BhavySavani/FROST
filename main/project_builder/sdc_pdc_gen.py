import json
import sys

free_pins = [1,2,3,4,5,6,7,8,9,10,13,14,15,16,19,20,21,22,24,27,28,29,30,32,33,36,37,38]

project_directory = sys.argv[1]
 
with open(f"{project_directory}/devices_config.json",'r') as f:
    device_config = json.load(f)

with open("main/protocol_config.json","r") as f:
    protocol_config = json.load(f)

io_str = ""
sdc_str = "create_clock -period 20 [get_ports clk]"
index = 0
io_str += "set_io clk -DIRECTION INPUT -pinname 23 -fixed yes\n"
for i in device_config["devices"]:
    for j in protocol_config["protocols"]:
        if j["protocol"] == i["protocol"]:
            inputs = j["inputs"]
            outputs =j["outputs"]
            if j["protocol"] == "i2c":
                inout = j["inout"]
                for ino in inout:
                    io_str +=(f"set_io {i["name"]}_{j["protocol"]}_{ino} -DIRECTION INOUT -pinname {free_pins[index]} -fixed yes\n")
                    index+=1
                
            for inp in inputs:
                if inp!= "clk":
                    io_str +=(f"set_io {i["name"]}_{j["protocol"]}_{inp} -DIRECTION INPUT -pinname {free_pins[index]} -fixed yes\n")
                    index+=1
            for out in outputs:
                io_str+=(f"set_io {i["name"]}_{j["protocol"]}_{out} -DIRECTION OUTPUT -pinname {free_pins[index]} -fixed yes\n")
                index+=1

with open(f"{project_directory}/mkr.pdc","w") as f:
    f.write(io_str)
with open(f"{project_directory}/mkr.sdc","w") as f:
    f.write(sdc_str)
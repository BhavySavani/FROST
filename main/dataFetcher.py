import json

def extractFPGAData():
    with open("main/supportedFPGA.json", 'r') as f:
        fpga_data = json.load(f)
    part_numbers = [fpga['part'] for fpga in fpga_data['fpgas']]
    return part_numbers

def getFPGAInfo(part_number):
    with open("main/supportedFPGA.json", 'r') as f:
        fpga_data = json.load(f)
    for fpga in fpga_data['fpgas']:
        if fpga['part'] == part_number:
            return [fpga['family'],fpga['software'],fpga['clock']]
    return None

def getDevicesList():
    with open("main/supportedDevices.json", 'r') as f:
        devices_data = json.load(f)
    devices = [device['name'] for device in devices_data['devices']]
    return devices

def getProtocols(device_name):
    with open("main/supportedDevices.json", 'r') as f:
        devices_data = json.load(f) 
    for device in devices_data['devices']:
        if device['name'] == device_name:
            return device['protocol']
    return None

def getProtocolDetails(device_name,protocol_name):
    with open("main/supportedDevices.json", 'r') as f:
        devices_data = json.load(f)
    for i in devices_data['devices']:
        if i['name'] == device_name:
            if "uart" == protocol_name:
                print(i['baud_rate'])
                return i['baud_rate']
            else:
                print(i['frequency'])
                return i['frequency']
                    
def addrFetcher(device_name):
    with open("main/supportedDevices.json", 'r') as f:
        devices_data = json.load(f)
    for i in devices_data['devices']:
        if i['name'] == device_name:
            return i["address"]
            
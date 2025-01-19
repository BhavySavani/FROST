import json

def extractFPGAData():
    with open("SupportedFPGA.json", 'r') as f:
        fpga_data = json.load(f)
    part_numbers = [fpga['part'] for fpga in fpga_data['fpgas']]
    return part_numbers

def getFPGAInfo(part_number):
    with open("SupportedFPGA.json", 'r') as f:
        fpga_data = json.load(f)
    for fpga in fpga_data['fpgas']:
        if fpga['part'] == part_number:
            return [fpga['family'],fpga['software'],fpga['clock']]
    return None

def getDevicesList():
    with open("SupportedDevices.json", 'r') as f:
        devices_data = json.load(f)
    devices = [device['name'] for device in devices_data['devices']]
    return devices

def getProtocols(device_name):
    with open("SupportedDevices.json", 'r') as f:
        devices_data = json.load(f) 
    for device in devices_data['devices']:
        if device['name'] == device_name:
            return device['protocols']
    return None

def getProtocolDetails(device_name,protocol_name):
    with open("SupportedProtocols.json", 'r') as f:
        devices_data = json.load(f)
    if device_name in devices_data['devices']:
        if protocol_name == 'i2c':
            return [devices_data['devices'][device_name]['frequency'],devices_data['devices'][device_name]['address']]
        if protocol_name == 'uart':
            return devices_data['devices'][device_name]['baudrate']
        else:
            return devices_data['devices'][device_name]['frequency']


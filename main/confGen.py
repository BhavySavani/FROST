import json
def confGenerate(deviceSelected):
    devicesDict={
      "clk": 50000000,
      "devices": []
    }

    #for i in range(len(deviceSelected)):
        protocol=protocolFetch(deviceSelected[i])
        freq=freqFetch(deviceSelected[i])
        '''for k in range(len(protocol)):
            if protocol[k] == "SPI" || protocol[k] == "RS485":
                for j in range(noOfDevices[i]):
                    devicesDict["devices"].append({
                    "name": deviceSelected[i]+"_"+str(noOfDevices[i]),
                    "protocol": protocol[k]
                    
                })
            else :
                for j in range(noOfDevices[i]):
                    devicesDict["devices"].append({
                    "name": deviceSelected[i]+"_"+str(noOfDevices[i]),
                    "protocol": protocol[k],
                    "frequency": freq
                })
        else:
            for j in range(noOfDevices[i]):
                devicesDict["devices"].append({
                "name": deviceSelected[i]+"_"+str(noOfDevices[i]),
                "protocol": protocol,
                "frequency": freq
        })
    with open("device_config.json","w") as f:
        json.dump(devicesDict,f)'''
    
    print(devicesDict)

def protocolFetch(dev):
    

def freqFetch(dev):
    pass

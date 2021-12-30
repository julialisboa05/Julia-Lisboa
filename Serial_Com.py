import struct
import csv
import serial
import time


def which_mode(Name):
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"] == Name:
                if row["Mode"] == "AOO":
                    return 0
                elif row["Mode"] == "VOO":
                    return 1
                elif row["Mode"] == "AAI":
                    return 2
                elif row["Mode"] == "VVI":
                    return 3
                elif row["Mode"] == "DOO":
                    return 4
                elif row["Mode"] == "AOOR":
                    return 5
                elif row["Mode"] == "VOOR":
                    return 6
                elif row["Mode"] == "AAIR":
                    return 7
                elif row["Mode"] == "VVIR":
                    return 8
                elif row["Mode"] == "DOOR":
                    return 9  

def pack_data(Name):
    SYNC = b'\x16'
    FN_CODE = b'\x55' #Set in simulink to write data
    pack_mode = which_mode(Name)
    
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"] == Name:
                
                LRL = int(row["LRL"])
                URL = int(row["URL"])
                AA = float(row["AA"])
                APW = float(row["APW"])
                AS = float(row["AS"])
                ARP = int(row["ARP"])
                PVARP = int(row["PVARP"])
                VA = float(row["VA"])
                VPW = float(row["VPW"])
                VS = float(row["VS"])
                VRP = int(row["VRP"])
                Hyst = int(row["Hyst"])
                RS = int(row["RS"])
                AVD = float(row["AVD"])
                MSR = float(row["MSR"])
                AT = float(row["AT"])
                React = float(row["React"])
                RF = float(row["RF"])
                Recover = float(row["Recover"])
                ID = int(row["ID"])
                break
            
    send = struct.pack("<ccBBBfffhhfffhBBffffffB", SYNC, FN_CODE, pack_mode, LRL, URL, AA, APW, AS, ARP, PVARP, VA, VPW, VS, VRP, Hyst, RS, AVD, MSR, AT, React, RF, Recover, ID)
    return send

def unpack_data(sent_string):
    received = struct.unpack("<BBBfffhhfffhBBffffffB", sent_string)
    return received            

def send(to_send):

    ser = serial.Serial()
    ser.baudrate = 115200 #set baudrate 
    ser.port = "COM4" 
    ser.open()
    ser.write(to_send) #write string which will be given from the pack_data
    ser.close() #close port

def receive():

    #same set up as send
    SYNC = b'\x16'
    FN_CODE = b'\x22' #set in simulink to get data back 
    ser = serial.Serial()
    ser.baudrate = 115200 
    ser.port = "COM4" 
    ser.open()
    
    get_back = struct.pack("<ccBBBfffhhfffhBBffffffB", SYNC, FN_CODE, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    ser.write(get_back)

    s = ser.read(60) #we are sending 60 bytes so we want to receive 60 back and only read until then
    back = unpack_data(s)
    
    return back #return what we read from the port and then we can use in unpack_data

'''
print(pack_data("test"))
send(pack_data("test"))

time.sleep(2)

print(receive())
'''

def get_egram():
    SYNC = b'\x16'
    FN_CODE = b'\x33' #set in simulink to get data back

    ser = serial.Serial()
    ser.baudrate = 115200 
    ser.port = "COM4" 
    ser.open()
    
    get_back = struct.pack("<ccBBBfffhhfffhBBffffffB", SYNC, FN_CODE, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    ser.write(get_back)

    s = ser.read(1600)
    atr_list = []
    vent_list = []
    for i in range(0, 1600, 32):
        atr = struct.unpack("d", s[i:i+8])[0]
        vent = struct.unpack("d", s[i+8:i+16])[0]   
        atr_list.append(atr)
        vent_list.append(vent)
        
    
    return atr_list, vent_list #return what we read from the port and then we can use in unpack_data


#print(get_egram())




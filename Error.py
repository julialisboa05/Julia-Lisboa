import PySimpleGUI as sg
import csv

sg.theme('DarkBrown4')

def pw_error(error):

    if error == 'mismatch':
        layout = [[sg.Text('Passwords do not match')],[sg.Button('Try Again')]]
    elif error == 'incorrect':
        layout = [[sg.Text('Incorrect patient name / password')],[sg.Button('Try Again')]]
    elif error == 'mode':
        layout = [[sg.Text('Invalid mode input')],[sg.Button('Try Again')]]
    window = sg.Window('Error',layout)
    while True:
        event, values = window.read()
        if event == 'Try Again':
            break
    window.close()

#trying with lists input
def range_error(user_input, para): #value is user input, para means parameter
    #pulse width has not error catching bc should just be a multiple
    #pulse amplitude acceptable values are modifed
    error_msg = []
    for i in range(len(user_input)):
        
        if user_input[i] == '' or user_input[i] == ' ':
            error = True
        else:
        
            value = float(user_input[i])
            error = False #initializing error state
           
            if para[i] == 'LRL' or para[i] == 'Hyst': #checking lower rate limit or hysteresis programmable values
                if value < 30 or value > 175:
                    error = True
                    if para[i] == 'LRL':
                        error_msg.append("LRL")
                    elif para[i] == 'Hyst':
                        error_msg.append("Hyst")
                elif value <= 50 or value >= 90: # checking if between 30-50 or 90-175
                    if ((value%5)!=0): # ensure the values are multiples of 5
                        error = True
                        if para[i] == 'LRL':
                            error_msg.append("LRL")
                        elif para[i] == 'Hyst':
                            error_msg.append("Hyst")
                elif value > 50 and ((value%1)!=0): #checking if between 50-90 and multiple of 1
                    error = True
                    if para[i] == 'LRL':
                        error_msg.append("LRL")
                    elif para[i] == 'Hyst':
                        error_msg.append("Hyst")

            elif para[i] == 'URL': #checking if upper rate limit is in programmable values
                if value < 50 or value > 175 or (value%5)!=0 :
                    error = True
                    error_msg.append("URL")
                    
            elif para[i] == 'MSR': #checking if max sensor rate is in programmable values
                if value < 50 or value > 175 or (value%5)!=0:
                    error = True
                    error_msg.append("MSR")

            elif para[i] == 'AVD': #checking if upper rate limit is in programmable values
                if value < 70 or value > 300 or (value%10)!=0:
                    error = True
                    error_msg.append("AVD")

            elif para[i] == 'AS' or para[i] == 'VS': #checking if AS/VS are equal are in range
                
                if value < 0 or value > 5:
                    error = True
                    if para[i] == 'AS':
                        error_msg.append("AS")
                    elif para[i] == 'VS':
                        error_msg.append("VS")

            elif para[i] == 'VRP' or para[i] == 'ARP' or para[i] == 'PVARP': #checking if VRP / ARP /PVARP are in range
                if value < 150 or value > 500 or (value%10)!=0:
                    error = True
                    if para[i] == 'VRP':
                        error_msg.append("VRP")
                    elif para[i] == 'ARP':
                        error_msg.append("ARP")
                    elif para[i] == 'PVARP':
                        error_msg.append("PVARP")

            elif para[i] == 'AA' or para[i] == 'VA': #checking if amplitude values are acceptable
                if value < 0.1 or value > 5:
                    error = True
                    if para[i] == 'AA':
                        error_msg.append("AA")
                    elif para[i] == 'VA':
                        error_msg.append("VA")
                        
            elif para[i] == 'APW' or para[i] == 'VPW':
                if value != 0.05:
                    if value < 1 or value > 30:
                        error == True
                        if para[i] == 'APW':
                            error_msg.append("APW")
                        elif para[i] == 'VPW':
                            error_msg.append("VPW")
                    
                            
            elif para[i] == "RS": #One of the values listed is off? Should we just call that zero? Also 25%?
                
                if (value%3) != 0:      #check if its divisible by 3
                    error == True
                    error_msg.append("RS")
                elif value < 0 or value > 21:   #check if its between 3 and 21 or off
                    error == True
                    error_msg.append("RS")

            elif para[i] == "React":
                #10-50 mult of 10
                if value < 10 or value > 50:
                    error == True
                    error_msg.append("React")
                elif int(value%10) != 0:
                    error == True
                    error_msg.append("React")

            elif para[i] == "RF":
                if value < 1 or value > 16:
                    error == True
                    error_msg.append("RF")
                elif value%1 != 0:
                    error == True
                    error_msg.append("RF")

            elif para[i] == "Recover":
                if value < 2 or value > 16:
                    error == True
                    error_msg.append("Recover")
                elif (value%1) != 0:
                    error == True
                    error_msg.append("Recover")
                    
    if len(error_msg) != 0: #checking if there were any errors
        layout = [[sg.Text('Inputted parameter '+ str(error_msg) +' is out of range')],[sg.Button('Try Again')]]
        window = sg.Window('Error',layout)
        while True:
            event, values = window.read()
            if event == 'Try Again':
                break
        window.close()
    return error, error_msg



def para_filled(Name):            #check that all necessary parameters are filled before a simulation runs
    
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

        flag = True     #initially set to true
        
        for row in reader:
            if row["Name"] == Name:   #find the row with patient we want
                                      #flag to false if any necessary columns are blank
                
                if row["URL"] == " " or row["LRL"] == " ":
                    flag = False       
                    
                if row["Mode"] == "AOO":
                    if row["AA"] == " " or row["APW"] == " ":
                        flag = False
                            
                elif row["Mode"] == "VOO":
                    if row["VA"] == " " or row["VPW"] == " ":
                        flag = False
                            
                elif row["Mode"] == "AAI":
                    if row["AA"] == " " or row["APW"] == " " or row["AS"] == " " or row["ARP"] == " " or row["PVARP"] == " " or row["Hyst"] == " " or row["RS"] == " ":
                        flag = False
                            
                elif row["Mode"] == "VVI":
                    
                    if row["VA"] == " " or row["VPW"] == " " or row["VS"] == " " or row["VRP"] == " " or row["Hyst"] == " " or row["RS"] == " ":
                        flag = False
                            
    return flag       #return true or false to use as parameter in if statement in data.py
                
                
    
    
    
    
    

                
        
        

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

def range_error(user_input, para): #value is user input, para means parameter
    #pulse width has not error catching bc should just be a multiple
    #pulse amplitude acceptable values are modifed
    if user_input == '' or user_input == ' ':
        error = True
    else:
        
        value = float(user_input)
        error = False #initializing error state
        if para == 'LRL' or para == 'Hyst': #checking lower rate limit or hysteresis programmable values
            if value < 30 or value > 175:
                error = True
            elif value <= 50 or value >= 90: # checking if between 30-50 or 90-175
                if ((value%5)!=0): # ensure the values are multiples of 5
                    error = True
            elif value > 50 and ((value%1)!=0): #checking if between 50-90 and multiple of 1
                error = True

        elif para == 'URL': #checking if upper rate limit is in programmable values
            if value < 50 or value > 175:
                error = True

        elif para == 'AS' or para == 'VS': #checking if AS/VS are equal are in range
            if value != 0.25 or value != 0.5 or value != 0.75:
                if value < 1 or value > 10:
                    error = True

        elif para == 'VRP' or para == 'ARP' or para == 'PVARP': #checking if VRP / ARP /PVARP are in range
            if value < 150 or value > 500:
                error = True

        elif para == 'AA' or para == 'VA': #checking if amplitude values are acceptable
            if value < 0.5 or value > 5:
                error = True

    if error == True: #checking if there were any errors
        layout = [[sg.Text('Inputted parameter is out of range')],[sg.Button('Try Again')]]
        window = sg.Window('Error',layout)
        while True:
            event, values = window.read()
            if event == 'Try Again':
                break
        window.close()
    return error

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
                
                
    
    
    
    
    
    
    

                
        
        

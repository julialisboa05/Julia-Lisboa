import PySimpleGUI as sg
import csv
import Error as pw_err
import data

sg.theme('DarkBrown4')

def login():
    layout = [[sg.Text('Patient Name:', font =('Arial', 20), size=(15, 1)), sg.InputText()],
            [sg.Text('Password:', font =('Arial', 20), size=(15, 1)), sg.InputText()],
            [sg.Button('Submit')]]
    window = sg.Window('Existing Patient', layout) #setting up layout
    while True: #reading the window
            event, values = window.read()
            if event == 'Submit':
                with open('Demo.csv', mode='r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["Name"] == values[0] and row["Password"] == values[1]: #checking if patient name / pw match
                        
                            found = True #call function that opens patient info tab have it return true, for now just set to true until fnction made 
                            window.close()
                            data.printing(row["Name"]) #call data file to display patient info
                            break
                        else:
                            found = False
                    if found != True:
                        pw_err.pw_error('incorrect') #notifies user of incorrect pw / user and prompts to error to try again
                        window.close()
                        login() #opens window again
                        break
                    else:
                        break
    
                     

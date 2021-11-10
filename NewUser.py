import PySimpleGUI as sg
import csv
import Error as err
import Run
import os
import data
import ExistingUser as exu

sg.theme('DarkBrown4')

def new_patient():

    length = check_length() #for now, the length variable will be saved and represent the pacemaker model #, in reality, the pacemaker ID # will be obtained by checking the hardware
    #in the future, this will be some sort of load ID function that stores the hardware #
    
    if length <= 10:
        layout = [[sg.Text('Patient Name:', font =('Arial', 20), size=(15, 1)), sg.InputText()],
                  [sg.Text('New Password:', font =('Arial', 20), size=(15, 1)), sg.InputText()],
                  [sg.Text('Confirm Password:', font =('Arial', 20), size=(15, 1)), sg.InputText()],
                  [sg.Button('Submit')]]
        window = sg.Window('New Patient', layout)
        while True:
            event, values = window.read()
            info = [values[0],values[1]]
            if event == 'Submit':
                if values[1] != values[2]:
                    match = False
                    err.pw_error('mismatch') #if the password creation does not match opens new pw window file
                    window.close()
                    new_patient()
                else:
                    match = True
                break
        if match == True: #if password matched, write to file
            window.close()
            mode_input(values[0],values[1],length) #calls the next function that controls user parameter inputs, name and pw and ID are passed through to save so they can be rewritten in
        

def mode_input(name, pw,ID):
    modes =['AOO','VOO','AAI','VVI'] #possible modes in the drop down menu
    layout = [[sg.Text('Input Mode:',font=('Arial', 20)),sg.Combo(values=modes)],[sg.Button('Submit')]]
    window = sg.Window('New Patient Input',layout,size=(300, 100),element_justification='c')
    while True:
        event, values = window.read()
        if event == 'Submit':

            window.close()
          
            if  values[0] == "AOO": #redirects to a different function based on the user mode input
                AOO_input(name, pw,ID) # for now, the
            elif values[0] == "VOO":
                VOO_input(name, pw,ID)
            elif values[0] == 'AAI':
                AAI_input(name,pw,ID)
            elif values[0] == 'VVI':
                VVI_input(name,pw,ID)
            else:
                err.pw_error('mode')
                mode_input(name,pw,ID)
            break
    
#for AOO new user inputs
def AOO_input(name,pw,ID):        
    #window set up
    layout =[
        [sg.Text('Input Parameters',font=('Courier New', 30))],
        [sg.Text('Lower Rate Limit (ppm):',font=('Arial', 20)), sg.InputText()],
        [sg.Text('Upper Rate Limit (ppm):',font=('Arial', 20)), sg.InputText()],
        [sg.Text('Atrial Amplitude (V):',font=('Arial', 20)), sg.InputText()],
        [sg.Text('Atrial Pulse Width (ms):',font=('Arial', 20)), sg.InputText()],
        [sg.Button('Submit',font=('Arial', 20))]
    ]
    window= sg.Window('New User Parameter Input', layout, size=(500, 400))
    
    while True:
        event, values = window.read()
        info = [name, pw, 'AOO',values[0],values[1],values[2],values[3],' ',' ',' ',' ',' ',' ',' ',' ',' ', ID] #creates a list of the given values at the correct place
        if event == 'Submit':
            break
    window.close()
    
    check_para = ['LRL','URL','AA','APW']
    check_input = [values[0],values[1],values[2],values[3]]

    for i in range(len(check_para)): #goes through the list of values and check things out
        check = err.range_error(check_input[i],check_para[i])
        if check == True:
            AOO_input(name,pw,ID)
            break
        
    if check != True: 
        append_to_file(info)
    
    
#for VOO new user inputs  
def VOO_input(name,pw,ID):      
    #window set up
    layout = [[sg.Text('Input Parameters',font=('Courier New', 30))],
            [sg.Text('Lower Rate Limit (ppm):',font=('Arial', 20)), sg.InputText()],
            [sg.Text('Upper Rate Limit (ppm):',font=('Arial', 20)), sg.InputText()],
            [sg.Text('Ventricular Amplitude (V):',font=('Arial', 20)), sg.InputText()],
            [sg.Text('Ventricular Pulse Width (ms):',font=('Arial', 20)), sg.InputText()],
            [sg.Button('Submit',font=('Arial', 20))]]
    
    window = sg.Window('New Patient Input',layout)

    while True:
        event, values = window.read()
        info = [name, pw, 'VOO',values[0],values[1],' ',' ',' ',' ',' ',values[2],values[3],' ',' ',' ',' ',ID] # takes the user input and puts it in as a list, spaces are to skip cells in the csv
        if event == 'Submit':
            break
    window.close()
    
    check_para = ['LRL','URL','VA','VPW']
    check_input = [values[0],values[1],values[2],values[3]]

    for i in range(len(check_para)): #goes through the list of values and check things out
        check = err.range_error(check_input[i],check_para[i])
        if check == True:
            VOO_input(name,pw,ID)
            break
        
    if check != True: 
        append_to_file(info)

#for AAI new user inputs
def AAI_input(name,pw,ID):        
    #window set up
    layout = [[sg.Text("Input Parameters",font=('Courier New', 30))],
              [sg.Text("Lower Rate Limit (ppm):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Upper Rate Limit (ppm):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Atrial Amplitude (V):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Atrial Pulse Width (ms):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Atrial Sensitivity (mV):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("ARP (ms):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("PVARP (ms):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Hysteresis (ppm):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Rate Smoothing:",font=('Arial', 20)), sg.InputText()],
              [sg.Button('Submit',font=('Arial', 20))]]
    window= sg.Window('New User Parameter Input', layout)
    
    while True:
        event, values = window.read()
        info = [name, pw, 'AAI',values[0],values[1],values[2],values[3],values[4],values[5],values[6],' ',' ',' ',' ',values[7],values[8],ID]
        #creates a list of the given values at the correct place, ' ' ensure things are inputted at the correct location
        if event == 'Submit':
            break
    window.close()

    check_para = ['LRL','URL','AA','APW','AS','ARP','PVARP','Hyst'] # don't need to check rate smoothing at this point
    check_input = [values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7]]

    for i in range(len(check_para)): #goes through the list of values and check things out
        check = err.range_error(check_input[i],check_para[i])
        if check == True:
            AAI_input(name,pw,ID)
            break
    if check != True: 
        append_to_file(info)

#for VVI new user inputs
def VVI_input(name,pw,ID):        
    #window set up
    layout = [[sg.Text("Input Parameters",font=('Courier New', 30))],
              [sg.Text("Lower Rate Limit (ppm):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Upper Rate Limit (ppm):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Ventricular Amplitude (V):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Ventricular Pulse Width (ms):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Ventricular Sensitivity (mV):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("VRP (ms):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Hysteresis (ppm):",font=('Arial', 20)), sg.InputText()],
              [sg.Text("Rate Smoothing:",font=('Arial', 20)), sg.InputText()],
              [sg.Button('Submit',font=('Arial', 20))]]
    window= sg.Window('New User Parameter Input', layout)
    
    while True:
        event, values = window.read()
        info = [name, pw, 'VVI',values[0],values[1],' ',' ',' ',' ',' ',values[2],values[3],values[4],values[5],values[6],values[7],ID]
        #creates a list of the given values at the correct place, ' ' ensure things are inputted at the correct location
        if event == 'Submit':
            break
    window.close()

    check_para = ['LRL','URL','VA','VPW','VS','VRP','Hyst'] # don't need to check rate smoothing at this point
    check_input = [values[0],values[1],values[2],values[3],values[4],values[5],values[6]]

    for i in range(len(check_para)): #goes through the list of values and check things out
        check = err.range_error(check_input[i],check_para[i])
        if check == True:
            VVI_input(name,pw,ID)
            break
        
    if check != True: 
        append_to_file(info)
    
def append_to_file(info):
    with open('Demo.csv','a+', newline = '') as f: #reopen file in append mode to add new patient a+ and new patient parameters
        writer = csv.writer(f)
        writer.writerow(info)

    #opens confirmation window
    data.printing(info[0])

    
def check_length(): #ensures there's no more than 10 patients
    f = open("Demo.csv")
    lines = 0
    for row in f:
        lines += 1
    f.close
    if lines > 10: #ensure to include headers, makes sure there is no more than 10 patients and does not allow anymore to be added, if not creates an error window
        
        layout = [[sg.Text("There are too many patients!")],
                   [sg.Button("Existing Patient")],
                   [sg.Button("Exit")]]
                  
        window = sg.Window("Err", layout,element_justification='c')
                  
        while True:
            event, values = window.read()
            if event == 'Exit':
                window.close()
                break
            elif event == "Existing Patient":
                window.close()
                exu.login()
                break
        
        return lines 
    else:
        return lines



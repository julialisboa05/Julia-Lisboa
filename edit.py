import PySimpleGUI as sg
import csv
import data
import Error as err
import pandas as pd

sg.theme('DarkBrown4')

def row_num(Name):
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            if Name == row["Name"]:
                break
            count +=1
    return count

def to_edit(Name):
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)
        
        mode_change(Name)
        
        for row in reader:
            if row["Name"] == Name:
                
                if row["Mode"] == "AOO":
                    AOO_change(Name)
                elif row["Mode"] == "VOO":
                    VOO_change(Name)
                elif row["Mode"] == "AAI":
                    AAI_change(Name)
                elif row["Mode"] == "VVI":
                    VVI_change(Name)
                    

def mode_change(Name):
    
    layout = [[sg.Text("Would you like to change modes?",font =("Arial",20))],
              [sg.Button("Yes",font =("Arial",15))],
              [sg.Button("No",font =("Arial",15))]]
    window = sg.Window("Mode Change", layout,element_justification='c')     #find out if they would like to change modes
    event, values = window.read()
    
    if event == "Yes":          #if yes display mode options
        window.close()
        modes =['AOO','VOO','AAI','VVI']      #possible modes in the drop down menu
        layout = [[sg.Text("Select new mode",font =("Arial",20))],
                  [sg.Combo(values=modes)],
                  [sg.Button('Submit',font =("Arial",20))]]
        
        window = sg.Window('Select Mode',layout,element_justification='c')
        event, values = window.read()
        
        if values[0] == '':
            print("yes")
            err.pw_error('mode')
            
        else:
            #write new mode to the csv file
            df = pd.read_csv("Demo.csv")
            df.at[row_num(Name),"Mode"] = values[0]
            df.to_csv("Demo.csv", index=False)
        
        if event == "Submit":
            window.close()
        
            data.printing(Name)       #bring back to data display with new mode/corresponding parameters
       
    elif event == "No":       #if no close window and allow to_edit function to continue as normal
        window.close()
        
                    
def VOO_change(Name):   
    
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"] == Name:   #find the row with patient we want
    
                layout = [[sg.Text("Parameters to change:",font =("Arial",20))],
                          [sg.Checkbox("LRL:",font=('Arial', 15),text_color='White'),sg.Text(row["LRL"],font=('Arial', 15))],
                          [sg.Checkbox("URL:",font=('Arial', 15),text_color='White'),sg.Text(row["URL"],font=('Arial', 15))],
                          [sg.Checkbox("VA:",font=('Arial', 15),text_color='White'),sg.Text(row["VA"],font=('Arial', 15))],
                          [sg.Checkbox("VPW:",font=('Arial', 15),text_color='White'),sg.Text(row["VPW"],font=('Arial', 15))],
                          [sg.Button("OK",font=('Arial', 15))]]
                break
        
    window = sg.Window('To Edit', layout)
    event, values = window.read()
    if event == "OK":
        window.close()
        
    layout = []
    changed = []
    
    #use if statements to see if any of the boxes are checked
    #if it is checked, add the corresponding parameter to layout so we can ask for the new value
    #if it is checked, add the column name to changed to keep track of what needs to be overwritten
    if values[0]:
        layout.append([sg.Text("LRL:",font=('Arial', 15)), sg.InputText()])
        changed.append("LRL")
    if values[1]:
        layout.append([sg.Text("URL:",font=('Arial', 15)), sg.InputText()])
        changed.append("URL")
    if values[2]:
        layout.append([sg.Text("VA:",font=('Arial', 15)), sg.InputText()])
        changed.append("VA")
    if values[3]:
        layout.append([sg.Text("VPW",font=('Arial', 15)), sg.InputText()])
        changed.append("VPW")
        
    layout.append([sg.Button('Submit',font=('Arial', 15))])
    
    window = sg.Window('Editing', layout)
    event, values = window.read()
    if event == "Submit":
        window.close()
        
    for i in range(len(changed)): #goes through the list of values and check of user input is valid
        check = err.range_error(values[i],changed[i])
        if check == True:
            VOO_change(Name)
            break
        
    df = pd.read_csv("Demo.csv")
    
    #for each entry in changed use the row number, changed entry, and value entry to overwrite the necesary parameters in csv file
    if check == False:
        for i in range(len(changed)):
            df.at[row_num(Name),changed[i]] = values[i]
            df.to_csv("Demo.csv", index=False)
        
    data.printing(Name)
                
def AOO_change(Name):  
    
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"] == Name:   #find the row with patient we want
    
                layout = [[sg.Text("Parameters to change:",font=('Arial', 20))],
                          [sg.Checkbox("LRL:",font=('Arial', 15),text_color='White'),sg.Text(row["LRL"],font=('Arial', 15))],
                          [sg.Checkbox("URL:",font=('Arial', 15),text_color='White'),sg.Text(row["URL"],font=('Arial', 15))],
                          [sg.Checkbox("AA:",font=('Arial', 15),text_color='White'),sg.Text(row["AA"],font=('Arial', 15))],
                          [sg.Checkbox("APW:",font=('Arial', 15),text_color='White'),sg.Text(row["APW"],font=('Arial', 15))],
                          [sg.Button("OK",font=('Arial', 15))]]
                break
        
    window = sg.Window('To Edit', layout)
    event, values = window.read()
    if event == "OK":
        window.close()
        
    changed = []
    layout = []
    
    if values[0]:
        layout.append([sg.Text("LRL:",font=('Arial', 15)), sg.InputText()])
        changed.append("LRL")
    if values[1]:
        layout.append([sg.Text("URL:",font=('Arial', 15)), sg.InputText()])
        changed.append("URL")
    if values[2]:
        layout.append([sg.Text("AA:",font=('Arial', 15)), sg.InputText()])
        changed.append("AA")
    if values[3]:
        layout.append([sg.Text("APW",font=('Arial', 15)), sg.InputText()])
        changed.append("APW")
        
    layout.append([sg.Button('Submit',font=('Arial', 15))])   
    
    window = sg.Window('Editing', layout)
    event, values = window.read()
    if event == "Submit":
        window.close()

    for i in range(len(changed)): #goes through the list of values and check of user input is valid
        check = err.range_error(values[i],changed[i])
        if check == True:
            AOO_change(Name)
            break
    
    df = pd.read_csv("Demo.csv")
    
    if check == False:
        for i in range(len(changed)):
            df.at[row_num(Name),changed[i]] = values[i]
            df.to_csv("Demo.csv", index=False)
        
    data.printing(Name)
       
def AAI_change(Name):
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"] == Name:   #find the row with patient we want
    
                layout = [[sg.Text("Parameters to change:",font=('Arial', 20))],
                          [sg.Checkbox("LRL:",font=('Arial', 15),text_color='White'),sg.Text(row["LRL"],font=('Arial', 15))],
                          [sg.Checkbox("URL:",font=('Arial', 15),text_color='White'),sg.Text(row["URL"],font=('Arial', 15))],
                          [sg.Checkbox("AA:",font=('Arial', 15),text_color='White'),sg.Text(row["AA"],font=('Arial', 15))],
                          [sg.Checkbox("APW:",font=('Arial', 15),text_color='White'),sg.Text(row["APW"],font=('Arial', 15))],
                          [sg.Checkbox("AS:",font=('Arial', 15),text_color='White'),sg.Text(row["AS"],font=('Arial', 15))],
                          [sg.Checkbox("ARP:",font=('Arial', 15),text_color='White'),sg.Text(row["ARP"],font=('Arial', 15))],
                          [sg.Checkbox("PVARP:",font=('Arial', 15),text_color='White'),sg.Text(row["PVARP"],font=('Arial', 15))],
                          [sg.Checkbox("Hyst:",font=('Arial', 15),text_color='White'),sg.Text(row["Hyst"],font=('Arial', 15))],
                          [sg.Checkbox("RS:",font=('Arial', 15),text_color='White'),sg.Text(row["RS"],font=('Arial', 15))],
                          [sg.Button("OK",font=('Arial', 15))]]
                break
        
    window = sg.Window('To Edit', layout)
    event, values = window.read()
    if event == "OK":
        window.close()
        
    layout = []
    changed = []
    
    if values[0]:
        layout.append([sg.Text("LRL:",font=('Arial', 15)), sg.InputText()])
        changed.append("LRL")
    if values[1]:
        layout.append([sg.Text("URL:",font=('Arial', 15)), sg.InputText()])
        changed.append("URL")
    if values[2]:
        layout.append([sg.Text("AA:",font=('Arial', 15)), sg.InputText()])
        changed.append("AA")
    if values[3]:
        layout.append([sg.Text("APW",font=('Arial', 15)), sg.InputText()])
        changed.append("APW")
    if values[4]:
        layout.append([sg.Text("AS",font=('Arial', 15)), sg.InputText()])
        changed.append("AS")
    if values[5]:
        layout.append([sg.Text("ARP",font=('Arial', 15)), sg.InputText()])
        changed.append("ARP")
    if values[6]:
        layout.append([sg.Text("PVARP",font=('Arial', 15)), sg.InputText()])
        changed.append("PVARP")
    if values[7]:
        layout.append([sg.Text("Hyst",font=('Arial', 15)), sg.InputText()])
        changed.append("Hyst")
    if values[8]:
        layout.append([sg.Text("RS",font=('Arial', 15)), sg.InputText()])
        changed.append("RS")
        
    layout.append([sg.Button('Submit',font=('Arial', 15))])   
    
    window = sg.Window('Editing', layout)
    event, values = window.read()
    if event == "Submit":
        window.close()    
    
    for i in range(len(changed)): #goes through the list of values and check of user input is valid
        check = err.range_error(values[i],changed[i])
        if check == True:
            AAI_change(Name)
            break
    
    df = pd.read_csv("Demo.csv")
    
    if check == False:
        for i in range(len(changed)):
            df.at[row_num(Name),changed[i]] = values[i]
            df.to_csv("Demo.csv", index=False)
        
    data.printing(Name)
    
    
def VVI_change(Name):
    
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"] == Name:   #find the row with patient we want
    
                layout = [[sg.Text("Parameters to change:",font=('Arial', 20))],
                          [sg.Checkbox("LRL:",font=('Arial', 15),text_color='White'),sg.Text(row["LRL"],font=('Arial', 15))],
                          [sg.Checkbox("URL:",font=('Arial', 15),text_color='White'),sg.Text(row["URL"],font=('Arial', 15))],
                          [sg.Checkbox("VA:",font=('Arial', 15),text_color='White'),sg.Text(row["VA"],font=('Arial', 15))],
                          [sg.Checkbox("VPW:",font=('Arial', 15),text_color='White'),sg.Text(row["VPW"],font=('Arial', 15))],
                          [sg.Checkbox("VS:",font=('Arial', 15),text_color='White'),sg.Text(row["VS"],font=('Arial', 15))],
                          [sg.Checkbox("VRP:",font=('Arial', 15),text_color='White'),sg.Text(row["VRP"],font=('Arial', 15))],
                          [sg.Checkbox("Hyst:",font=('Arial', 15),text_color='White'),sg.Text(row["Hyst"],font=('Arial', 15))],
                          [sg.Checkbox("RS:",font=('Arial', 15),text_color='White'),sg.Text(row["RS"],font=('Arial', 15))],
                          [sg.Button("OK",font=('Arial', 15))]]
                break
    
    window = sg.Window('To Edit', layout)
    event, values = window.read()
    if event == "OK":
        window.close()
        
    layout = []
    changed = []
    
    if values[0]:
        layout.append([sg.Text("LRL:",font=('Arial', 15)), sg.InputText()])
        changed.append("LRL")
    if values[1]:
        layout.append([sg.Text("URL:",font=('Arial', 15)), sg.InputText()])
        changed.append("URL")
    if values[2]:
        layout.append([sg.Text("VA:",font=('Arial', 15)), sg.InputText()])
        changed.append("VA")
    if values[3]:
        layout.append([sg.Text("VPW",font=('Arial', 15)), sg.InputText()])
        changed.append("VPW")
    if values[4]:
        layout.append([sg.Text("VS",font=('Arial', 15)), sg.InputText()])
        changed.append("VS")
    if values[5]:
        layout.append([sg.Text("VRP",font=('Arial', 15)), sg.InputText()])
        changed.append("VRP")
    if values[6]:
        layout.append([sg.Text("Hyst",font=('Arial', 15)), sg.InputText()])
        changed.append("Hyst")
    if values[7]:
        layout.append([sg.Text("RS",font=('Arial', 15)), sg.InputText()])
        changed.append("RS")
        
    layout.append([sg.Button('Submit',font=('Arial', 15))])   
    
    window = sg.Window('Editing', layout)
    event, values = window.read()
    if event == "Submit":
        window.close()
    
    for i in range(len(changed)): #goes through the list of values and check of user input is valid
        check = err.range_error(values[i],changed[i])
        if check == True:
            VVI_change(Name)
            break
        
    df = pd.read_csv("Demo.csv")
    
    if check == False:
        for i in range(len(changed)):
            df.at[row_num(Name),changed[i]] = values[i]
            df.to_csv("Demo.csv", index=False)
        
    data.printing(Name)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

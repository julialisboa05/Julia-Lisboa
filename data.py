import PySimpleGUI as sg
import csv
import Pacemaker_ID as pm_ID
import Error as err
import Run
import os
import edit

sg.theme('DarkBrown4')

def printing(Name_given):        #call with the name of patient
    
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"] == Name_given:   #find the row with patient we want

                #checks PM ID associated with name to see if it has been approached
                if pm_ID.ID_num(row["ID"]) == False:
                    err.pw_error('incorrect') #since there is no hardware yet, the only reason this would return false is when user is not recognized
                    os.system('Home.py')
                    exit()
                    break 
               
                if row["Mode"] == "AOO": #Display parameters for AOO
                   #pace maker recognized prints and confirms the device has been approached before
                    layout = [[sg.Text("Data Display",font=("Courier New",20))],[sg.Text("Pacemaker Recognized",font=('Arial', 15),text_color='White')],
                              [sg.Text(row["Name"],font=('Arial', 15))],
                              [sg.Text(row["Mode"],font=('Arial', 15),text_color='White')],
                              [sg.Text("Lower Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["LRL"],font=('Arial', 15))],
                              [sg.Text("Upper Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["URL"],font=('Arial', 15))],
                              [sg.Text("Atrial Amplitude:",font=('Arial', 15),text_color='White'), sg.Text(row["AA"],font=('Arial', 15))],
                              [sg.Text("Atrial Pulse Width:",font=('Arial', 15),text_color='White'), sg.Text(row["APW"],font=('Arial', 15))],
                              [sg.Button('Run Simulation',font=('Arial', 15)),sg.Button('Home',font=('Arial', 15)),sg.Button("Edit",font=('Arial', 15))]]     
                    
                    window = sg.Window("Data Display", layout,size = (500,350),element_justification='c')
                    event, values = window.read()
                    if event == "Home":                   
                        window.close()
                        os.system('Home.py')
                        exit()
                        break
                    elif event == "Run Simulation":
                        window.close()
                        if err.para_filled(Name_given):      #check all necessary parameters are filled
                            Run.running()
                        else:           #if not display error message
                            layout = [[sg.Text("Necessary parameters not filled")],
                                      [sg.Button("Back")]]
                            window = sg.Window("Error", layout)
                            event, values = window.read()
                            if event == "Back":         #and allow them to try again
                                window.close()
                                printing(Name_given)
                            
                    elif event == "Edit":
                        window.close()
                        edit.to_edit(Name_given)
                        break
                    
                elif row["Mode"] == "VOO":  #Display parameters for VOO
                    
                    layout = [[sg.Text("Data Display",font=("Courier New",20))],[sg.Text("Pacemaker Recognized",font=('Arial', 15),text_color='White')],
                              [sg.Text(row["Name"],font=('Arial', 15))],
                              [sg.Text(row["Mode"],font=('Arial', 15),text_color='White')],
                              [sg.Text("Lower Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["LRL"],font=('Arial', 15))],
                              [sg.Text("Upper Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["URL"],font=('Arial', 15))],
                              [sg.Text("Ventricular Amplitude:",font=('Arial', 15),text_color='White'), sg.Text(row["VA"],font=('Arial', 15))],
                              [sg.Text("Ventricular Pulse Width:",font=('Arial', 15),text_color='White'), sg.Text(row["VPW"],font=('Arial', 15))],
                              [sg.Button('Run Simulation',font=('Arial', 15)),sg.Button('Home',font=('Arial', 15)),sg.Button("Edit",font=('Arial', 15))]]   
                    
                    
                    window = sg.Window("Data Display", layout)
                    event, values = window.read()
                    if event == "Home":
                        window.close()
                        os.system('Home.py')
                        exit()
                        break
                    elif event == "Run Simulation":
                        window.close()
                        if err.para_filled(Name_given):
                            Run.running()
                        else:
                            layout = [[sg.Text("Necessary parameters not filled")],
                                      [sg.Button("Back")]]
                            window = sg.Window("Error", layout)
                            event, values = window.read()
                            if event == "Back":
                                window.close()
                                printing(Name_given)
                                
                    elif event == "Edit":
                        window.close()
                        edit.to_edit(Name_given)
                        break
                        
                elif row["Mode"] == "AAI":
                    
                    layout = [[sg.Text("Data Display",font=("Courier New",20))],[sg.Text("Pacemaker Recognized",font=('Arial', 15),text_color='White')],
                              [sg.Text(row["Name"],font=('Arial', 15))],
                              [sg.Text(row["Mode"],font=('Arial', 15),text_color='White')],
                              [sg.Text("Lower Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["LRL"],font=('Arial', 15))],
                              [sg.Text("Upper Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["URL"],font=('Arial', 15))],
                              [sg.Text("Atrial Amplitude:",font=('Arial', 15),text_color='White'), sg.Text(row["AA"],font=('Arial', 15))],
                              [sg.Text("Atrial Pulse Width:",font=('Arial', 15),text_color='White'), sg.Text(row["APW"],font=('Arial', 15))],
                              [sg.Text("Atrial Sensitivity:",font=('Arial', 15),text_color='White'), sg.Text(row["AS"],font=('Arial', 15))],
                              [sg.Text("ARP:",font=('Arial', 15),text_color='White'), sg.Text(row["ARP"],font=('Arial', 15))],
                              [sg.Text("PVARP:",font=('Arial', 15),text_color='White'), sg.Text(row["PVARP"],font=('Arial', 15))],
                              [sg.Text("Hysteresis:",font=('Arial', 15),text_color='White'), sg.Text(row["Hyst"],font=('Arial', 15))],
                              [sg.Text("Rate Smoothing:",font=('Arial', 15),text_color='White'), sg.Text(row["RS"],font=('Arial', 15))],
                              [sg.Button('Run Simulation',font=('Arial', 15)),sg.Button('Home',font=('Arial', 15)),sg.Button("Edit",font=('Arial', 15))]]     
                    
                    window = sg.Window("Data Display", layout)
                    event, values = window.read()
                    if event == "Home":
                        window.close()
                        os.system('Home.py')
                        exit()
                        break
                    elif event == "Run Simulation":
                        window.close()
                        if err.para_filled(Name_given):
                            Run.running()
                        else:
                            layout = [[sg.Text("Necessary parameters not filled")],
                                      [sg.Button("Back")]]
                            window = sg.Window("Error", layout)
                            event, values = window.read()
                            if event == "Back":
                                window.close()
                                printing(Name_given)
                                
                    elif event == "Edit":
                        window.close()
                        edit.to_edit(Name_given)
                        break
                        
                elif row["Mode"] == "VVI":
                    
                    layout = [[sg.Text("Data Display",font=("Courier New",20))],[sg.Text("Pacemaker Recognized",font=('Arial', 15),text_color='White')],
                              [sg.Text(row["Name"],font=('Arial', 15))],
                              [sg.Text(row["Mode"],font=('Arial', 15),text_color='White')],
                              [sg.Text("Lower Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["LRL"],font=('Arial', 15))],
                              [sg.Text("Upper Rate Limit:",font=('Arial', 15),text_color='White'), sg.Text(row["URL"],font=('Arial', 15))],
                              [sg.Text("Ventricular Amplitude:",font=('Arial', 15),text_color='White'), sg.Text(row["VA"],font=('Arial', 15))],
                              [sg.Text("Ventricular Pulse Width:",font=('Arial', 15),text_color='White'), sg.Text(row["VPW"],font=('Arial', 15))],
                              [sg.Text("Ventricular Sensitivity:",font=('Arial', 15),text_color='White'), sg.Text(row["VS"],font=('Arial', 15))],
                              [sg.Text("VRP:",font=('Arial', 15),text_color='White'), sg.Text(row["VRP"],font=('Arial', 15))],
                              [sg.Text("Hysteresis:",font=('Arial', 15),text_color='White'), sg.Text(row["Hyst"],font=('Arial', 15))],
                              [sg.Text("Rate Smoothing:",font=('Arial', 15),text_color='White'), sg.Text(row["RS"],font=('Arial', 15))],
                              [sg.Button('Run Simulation',font=('Arial', 15)),sg.Button('Home',font=('Arial', 15)),sg.Button("Edit",font=('Arial', 15))]]     
                    
                    window = sg.Window("Data Display", layout)
                    event, values = window.read()
                    if event == "Home":
                        window.close()
                        os.system('Home.py')
                        exit()
                        break
                    elif event == "Run Simulation":
                        window.close()
                        if err.para_filled(Name_given):   #only allow simulation to run if all parameters are filled
                            Run.running()
                        else:                      #if not filled display error message
                            layout = [[sg.Text("Necessary parameters not filled")],
                                      [sg.Button("Back")]]
                            window = sg.Window("Error", layout)
                            event, values = window.read()
                            
                            if event == "Back":
                                window.close()
                                printing(Name_given)          #and allow them to try again
                                
                    elif event == "Edit":
                        window.close()
                        edit.to_edit(Name_given)
                        break
                    
                break                     
    

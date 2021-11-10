import PySimpleGUI as sg
import csv
import os

def running(): 
    # loading bar from https://stackoverflow.com/questions/65575861/waiting-screen-while-data-is-being-extracted-from-an-api
    sg.theme('DarkBrown4')
    layout = [[sg.Text('', size=(50, 1), relief='sunken', font=('Courier', 15),text_color='yellow', background_color='black',key='TEXT')],[sg.Button('Cancel')]]
    window = sg.Window('Running', layout, finalize=True)
    text = window['TEXT']
    state = 0
    while True:

        event, values = window.read(timeout=100)

        if event == 'Cancel':
            window.close()
            os.system('Home.py')
            break
        state = (state+1)%51
        text.update('█'*state)

    window.close()

def load_parameters(Name_given): #ideally this function will pass the necessary parameters to the hardware, however, they are not connected yet so it returns nothing
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

    for row in reader:
        if row["Name"] == Name_given:   #find the row with patient we want
           
            if row["Mode"] == "AOO": #Display parameters for AOO

                LRL = int(row["LRL"])
                URL = int(row["URL"])
                AA = int(row["AA"])
                APW = int(row["APW"]) # in the future, when the program is connected to the hardware, these values will be passed through (may have to change type)
                
            elif row["Mode"] == "VOO":  #Display parameters for VOO

                LRL = int(row["LRL"])
                URL = int(row["URL"])
                VA = int(row["VA"])
                VPW = int(row["VPW"])
                
            elif row["Mode"] == "AAI":

                LRL = int(row["LRL"])
                URL = int(row["URL"])
                AA = int(row["AA"])
                APW = int(row["APW"])
                AS = int(row["AS"])
                ARP = int(row["ARP"])
                PVARP = int(row["PVARP"])
                HYST = int(row["Hyst"])
                RS = int(row["RS"])
                         
            elif row["Mode"] == "VVI":

                LRL = int(row["LRL"])
                URL = int(row["URL"])
                VA = int(row["VA"])
                VPW = int(row["VPW"])
                VS = int(row["VS"])
                VVP = int(row["VVP"])
                HYST = int(row["Hyst"])
                RS = int(row["RS"])
            break
    running()

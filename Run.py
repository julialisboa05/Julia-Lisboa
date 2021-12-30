import PySimpleGUI as sg
import csv
import Error as err
import os
import time
import Serial_Com as com
import struct
import egram

sg.theme('DarkBrown4')

def serial(Name):

    to_send = com.pack_data(Name)
    sending = struct.unpack("<ccBBBfffhhfffhBBffffffB", to_send)
    first_display = sending[2:]
    ID = first_display[-1]
    com.send(to_send)
    
    layout = [[sg.Text("Sending . . .",font=("Courier New",20))],
            [sg.Text("Parameters sent: "+str(first_display), font=('Arial', 15), text_color='White')],
            [sg.Text("Patient ID sent: "+str(ID),font=('Arial', 15), text_color='White')]]
    
    window = sg.Window("Data Display", layout, element_justification='c')
    event, values = window.read(timeout = 3000)

    window.close()
    
    received = com.receive()
    ID_2 = received[-1]

    layout = [[sg.Text("Received",font=("Courier New",20))],
            [sg.Text("Parameters sent: "+str(first_display), font=('Arial', 15), text_color='White')],
            [sg.Text("Patient ID sent: "+str(ID),font=('Arial', 15), text_color='White')],
            [sg.Text("Parameters received: "+str(received), font=('Arial', 15), text_color='White')],
            [sg.Text("Patient ID received: "+str(ID_2),font=('Arial', 15), text_color='White')]]

    if int(ID) == int(ID_2):
        layout.append([sg.Text("Pacemaker Recognized",font=("Courier New",20))])
    
    window = sg.Window("Data Display", layout, element_justification='c')
    event, values = window.read(timeout = 10000)

    window.close()    
    
    return None

def running(Name):
    
    serial(Name)
    # loading bar from https://stackoverflow.com/questions/65575861/waiting-screen-while-data-is-being-extracted-from-an-api
    sg.theme('DarkBrown4')
    layout = [[sg.Text('', size=(50, 1), relief='sunken', font=('Courier', 15),text_color='yellow', background_color='black',key='TEXT')],[sg.Button('Cancel')],
              [sg.Button("Show Egram")]]
    window = sg.Window('Running', layout, finalize=True)
    text = window['TEXT']
    state = 0
    while True:

        event, values = window.read(timeout=100)

        if event == 'Cancel':
            window.close()
            os.system('Home.py')
            break
        elif event == "Show Egram":
            window.close()
            egram.egram_choose()
            break
            
        state = (state+1)%51
        text.update('█'*state)

    window.close()

#running("Charlotte Neumann")




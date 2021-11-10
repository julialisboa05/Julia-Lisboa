import PySimpleGUI as sg
import NewUser as nu
import ExistingUser as exu
from emoji import emojize


def main():
    sg.theme('DarkBrown4')
    heart = "     " + emojize(":red_heart:") # adding simple emoji graphic
    layout = [[sg.Text("Pacemaker DCM",font=('Courier New',30))],
              [sg.Text(heart,font=('Arial',80))],
              [sg.Button("New Patient",font=('Arial', 20))],
              [sg.Button("Existing Patient",font=('Arial', 20))],
              [sg.Button("Exit",font=('Arial',20))]]
    window = sg.Window("Pacemaker DCM" , layout,size=(500, 400),element_justification='c')

    while True:
        event, values = window.read()
        if event == "New Patient":
            window.close()
            nu.new_patient()
            break
        elif event == "Existing Patient":
            window.close()
            exu.login()
            break
        elif event == "Exit":
            window.close()
            exit()
            break

main()

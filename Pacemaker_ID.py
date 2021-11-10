import PySimpleGUI as sg
import csv

def ID_num(ID): #passes pacemaker ID through
    with open('Demo.csv', mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["ID"] == ID:
                return True #function returns true if pacemaker has been approached 
        return False # function returns false if it has not been interrogated
    

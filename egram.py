import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import random
import Serial_Com as com
import os

#graphing code based on https://towardsdatascience.com/integrating-pyplot-and-pysimplegui-b68be606b960

# VARS CONSTS:
_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False}

dataSize = 300 #easy to fix
timestep = 3 #easy change

# Theme for pyplot and windows
plt.style.use('Solarize_Light2')
sg.theme('DarkBrown4')
xData = np.linspace(0, dataSize, num=dataSize, dtype=int) #define the x-axis of the plot


# prompts user to select which egram they wish
def egram_choose(): #select which egram must be run
    sg.theme('DarkBrown4')
    layout = [[sg.Text('Select which data you would like to display')],[sg.Button("Atrium"),sg.Button("Ventricle"),sg.Button("Both")]]
    window = sg.Window('egram', layout, element_justification='c')
    
    while True:
        event, values = window.read()

        if event == 'Atrium':
            window.close()
            egram_plot_a()
            break
        elif event =='Ventricle':
            window.close()
            egram_plot_v()
            break
        elif event == 'Both':
            window.close()
            egram_plot_both()
            break
    window.close()
    
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

#collects atrium data from hardware
def getData_a(atr_list):
    #atr, vtr = com.get_egram() #uncomment when want to actually run with serial
    atr = random.sample(range(1, 101), 100) #placeholder until get serial, if this range is less the the number of points, gets mad
    atr_list = np.append(atr_list,atr)
    print(atr_list[-dataSize:])
    atr_list = atr_list[-dataSize:]
    return (atr_list)

def getData_v(vtr_list): #collects ventricle data
    atr, vtr = com.get_egram() #uncomment when want to actually run with serial
    #vtr = random.sample(range(1, 101), 100) #placeholder until get serial, if this range is less the the number of points, gets mad
    vtr_list = np.append(vtr_list,vtr)
    #print(vtr_list[-dataSize:])
    vtr_list = vtr_list[-dataSize:]
    return (vtr_list)

def getData_both(atr_list, vtr_list): #gets data when plotting both
    atr, vtr = com.get_egram() #uncomment when want to actually run with serial
    #atr = random.sample(range(1, 101), 100) #placeholder until get serial, if this range is less the the number of points, gets mad
    #vtr = random.sample(range(1, 101), 100) #placeholder until get serial, if this range is less the the number of points, gets mad
    atr_list = np.append(atr_list,atr)
    vtr_list = np.append(vtr_list,vtr)
    atr_list = atr_list[-dataSize:]
    vtr_list = vtr_list[-dataSize:]
    return (atr_list, vtr_list)
    
#initializes chart
def drawChart(yData):
    _VARS['pltFig'] = plt.figure()
    plt.plot(xData, yData)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

#initializes chart for both
def drawChartBoth(atrData, ventData):
    _VARS['pltFig'], (ax1, ax2) = plt.subplots(2,sharex=True) #must use subplot instead since there are two things that must be graphed, sharex= True lets share xaxis
    ax1.plot(xData, atrData) #create atrium subplot
    ax2.plot(xData, ventData) #create ventricle subplot
    ax1.set(ylabel='Atrial Amplitude')
    ax2.set(ylabel='Ventricle Amplitude')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])
    
#called each time chart needs an update
def updateChart(yData):
    _VARS['fig_agg'].get_tk_widget().forget()
    # plt.cla()
    plt.clf()
    plt.plot(xData, yData)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

def updateChartBoth(atrData, ventData): #each time both chart needs an update, clear it similar to updateChart and resets properly
    _VARS['fig_agg'].get_tk_widget().forget()
    # plt.cla()
    plt.clf()
    _VARS['pltFig'], (ax1, ax2) = plt.subplots(2,sharex=True)
    ax1.plot(xData, atrData) #create atrium subplot
    ax2.plot(xData, ventData) #create ventricle subplot
    ax1.set(ylabel='Atrial Amplitude')
    ax2.set(ylabel='Ventricle Amplitude')
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])


# plots atrium data
def egram_plot_a():
    layout = [[sg.Text('Atrial Egram', size=(40, 1), pad=((300, 0), 3), font='Helvetica 30')],
          [sg.Canvas(key='figCanvas')],
          [sg.Button('Exit')]]
    _VARS['window'] = sg.Window('Atrium Data',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(100, 100),
                            element_justification="center")
    atr_list = np.zeros((dataSize+10,), dtype=int) #initialize an array of zeros with the necessary data size and more
    drawChart(atr_list[-dataSize:])
    while True:
        event, values = _VARS['window'].read(timeout=200)
        if event == 'Exit':
            _VARS['window'].close()
            os.system('Home.py')
            break
        time.sleep(timestep) #time between updates, can change
        atr_list = getData_a(atr_list)
        updateChart(atr_list)
    _VARS['window'].close()

def egram_plot_v(): #setting up window and plotting ventricle data
    layout = [[sg.Text('Ventricle Egram', size=(40, 1), pad=((300, 0), 3), font='Helvetica 30')],
          [sg.Canvas(key='figCanvas')],
          [sg.Button('Exit')]]
    _VARS['window'] = sg.Window('Ventricle Data',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(100, 100),
                            element_justification="center")
    vtr_list = np.zeros((dataSize+10,), dtype=int) #initialize an array of zeros with the necessary data size and more
    drawChart(vtr_list[-dataSize:])
    while True:
        event, values = _VARS['window'].read(timeout=200)
        if event == 'Exit':
            _VARS['window'].close()
            os.system('Home.py')
            break
        time.sleep(timestep) #time between updates, can change
        vtr_list = getData_v(vtr_list)
        updateChart(vtr_list)
    _VARS['window'].close()

def egram_plot_both():
    layout = [[sg.Text('Egram', size=(40, 1), pad=((300, 0), 3), font='Helvetica 30')],
          [sg.Canvas(key='figCanvas')],
          [sg.Button('Exit')]]
    _VARS['window'] = sg.Window('Atrium and Ventricle Data',
                            layout,
                            finalize=True,
                            resizable=True,
                            location=(100, 100),
                            element_justification="center")
    atr_list = np.zeros((dataSize+10,), dtype=int)
    vtr_list = np.zeros((dataSize+10,), dtype=int) #initialize an array of zeros with the necessary data size and more
    drawChartBoth(atr_list[-dataSize:],vtr_list[-dataSize:]) #calls its own both function, passes both data sets through
    while True:
        event, values = _VARS['window'].read(timeout=200)
        if event == 'Exit':
            _VARS['window'].close()
            os.system('Home.py')
            break
        time.sleep(timestep) #time between updates, can change
        atr_list, vtr_list = getData_both(atr_list, vtr_list) #returns both lists and stores them
        updateChartBoth(atr_list, vtr_list)
    _VARS['window'].close()
    

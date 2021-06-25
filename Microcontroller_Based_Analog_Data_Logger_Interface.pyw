from win10toast import ToastNotifier
from time import time
from serial import Serial
import numpy as np
import pandas as pd
import plotly.graph_objects as go
toaster = ToastNotifier()
port = 'COM3'
try:
    ser = Serial(port)
except:
    while True:
        if toaster.show_toast('Connect to the microcontroller via USB', ' ', 
                              threaded = True):
            break
        try:
            ser = Serial(port)
            break
        except:
            pass
    try:
        ser
    except:
        while True:
            try:
                ser = Serial(port)
                break
            except:
                pass
connected_tick = time()
while True:
    connected_tock = time()
    connected_time = connected_tock - connected_tick
    if toaster.show_toast('Microcontroller connected %.1f seconds ago'
                          % connected_time,
                          'Starting now, you may disconnect',
                          threaded = True):
        break
    try:
        ser.readline()
    except:
        try:
            disconnected_tick
        except:
            disconnected_tick = time()
lines = []
while True:
    try:
        lines.append(ser.readline())
    except:
        break
try:
    disconnected_tick
except:
    disconnected_tick = time()
while True:
    disconnected_tock = time()
    disconnected_time = disconnected_tock - disconnected_tick
    if toaster.show_toast('Microcontroller disconnected %.1f seconds ago' % disconnected_time, ' ', threaded = True):
        break
y = np.array([float(line[:-2]) for line in lines[1:-1]])
Dt = 10e-3
t = np.arange(len(y)) * Dt
window = 100
y_smooth = pd.Series(y).rolling(window, center = True).mean().to_numpy()
np.savetxt('data.csv', y, fmt = '%.1f')
data = go.Scatter(x = t, y = y_smooth)
fig = go.Figure(data)
fig.update_layout(xaxis_title = 'Time in Seconds', yaxis_title = 'Logged Data')
fig.update_layout(title = 'Logged Data')
fig.show()

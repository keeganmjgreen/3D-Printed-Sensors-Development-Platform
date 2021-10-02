from serial    import Serial
from threading import Thread

####################################################################################################

fname = 'Force_Sensor_Calibration_Data_Log.txt'

while True:
    
    port = 'COM' + input('Enter serial communications port (e.g., COM1) : COM')
    
    try:
        ser = Serial(port)
    except:
        print('COM port invalid or unavailable.')
    else:
        break

lines = []

def logger():
    print('Type markers...')
    print('DO NOT STOP THE PROGRAM BEFORE DISCONNECTING YOUR MICROCONTROLLER')
    while True:
        lines.append(input('Marker: '))

Thread(target = logger).start()

while True:
    try:
        lines.append(ser.readline().decode()[:-2])
    except:
        break

with open(fname, 'w') as buffer:
    for line in lines[1:-1]:
        buffer.write(line + '\n')

print(f'Microcontroller disconnected. {fname} saved. You may now close the program.')

while True:
    pass

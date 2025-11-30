import serial
import matplotlib.pyplot as plt
from collections import deque

# Set the correct COM port and baud rate
# On Windows: 'COM3', 'COM4', etc.
# On Linux/macOS: '/dev/ttyACM0' or '/dev/ttyUSB0'
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Prepare plot
plt.ion()  # interactive mode
fig, ax = plt.subplots()
window_size = 100
data = deque([0]*window_size, maxlen=window_size)
line, = ax.plot(range(window_size), data)
ax.set_ylim(0, 65535)  # ADC range

while True:
    try:
        line_str = ser.readline().decode('utf-8').strip()
        if line_str:
            val = int(line_str)
            data.append(val)
            line.set_ydata(data)
            plt.pause(0.01)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)

ser.close()

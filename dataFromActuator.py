import serial
import time
import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM14')
ser.flushInput()

"""`1plot_window = 20
y_var = np.array(np.zeros([plot_window]))

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(y_var)"""

while True:
    try:
        ser_bytes = ser.readline()
        try:
            decoded_bytes = ser_bytes.split()
            decoded_bytes[0] = decoded_bytes[0].decode("utf-8")
            decoded_bytes[1] = decoded_bytes[1].decode("utf-8")
            #print(decoded_bytes)
        except:
            continue
        tt = time.time()
        with open("angleRespect.csv","a") as f:
            writer = csv.writer(f,delimiter=" ")
            writer.writerow([tt, decoded_bytes[0]])

        with open("accRespect.csv","a") as f:
            writer = csv.writer(f,delimiter=" ")
            writer.writerow([tt, decoded_bytes[1]])
        """y_var = np.append(y_var,decoded_bytes)
        y_var = y_var[1:plot_window+1]
        line.set_ydata(y_var)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()"""
    except:
        print("Keyboard Interrupt")
        break
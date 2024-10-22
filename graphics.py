import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
with open('data_1', 'r') as f:
    for line in f:
        x.append(int(line))

with open('settings_1', 'r') as settings:
    lines = [line for line in settings]

#print(lines)
#l1 = lines[0].split()
#print(l1)
time_step = float(lines[0])
#print(frequency)
qv = float(lines[1])
#print(qv)
voltage = []
for i in range(len(x)):
    voltage.append(x[i]*qv)
time_1 = []
voltage_1 = []

time = []
t = 0
for i in range(len(voltage)):
    time.append(t)
    t += time_step
for i in range(0, len(voltage), 50):
    voltage_1.append(voltage[i])
    time_1.append(time[i])
for i in range(len(voltage)):
    if (voltage[i] == max(voltage)):
        number_of_maximum = i
time_of_maximum = time[number_of_maximum]
time_of_minimum = time[len(time)-1]-time_of_maximum
print(time_of_maximum)
print(time_of_minimum)
fig = plt.figure(figsize=(6, 10))
ax = plt.subplot()
plt.plot(time, voltage, 'r-^', markevery = 50, color = 'magenta', linewidth = 0.9)
#plt.plot(time_1, voltage_1, 'm-^', linestyle = 'none')
plt.xlabel('Time, sec')
plt.ylabel('Voltage, V')
#plt.grid(b = True, which = 'both', color = 'black', linewidth = 0.5.
ax.grid(which = "major", linewidth = 1)
ax.minorticks_on()
ax.grid(which = "minor", linewidth = 0.3)
ax.set_ylim(min(voltage), max(voltage))
ax.set_xlim(min(time), max(time))
#strings = 'Time to charge the capacitor: '
plt.text(6, 2.5, 'Time to charge the capacitor: 5.13 s', fontsize = 8.5)
plt.text(6, 2.35, 'Time to uncharge the capacitor: 6.9 s', fontsize = 8.5)
plt.title('Dependence of voltage on time')
plt.show()
fig.savefig('graphics.svg', dpi=fig.dpi)

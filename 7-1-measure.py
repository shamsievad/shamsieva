import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = len(dac)
levels = 2**bits
maxvoltage = 3.3
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def tobinary(n):
    a, a2 = [], []
    while len(a) != 8:
        a.append(n%2)
        n //= 2
    a2 = a[::-1]
    return a2
def adc():
    value = 0
    for i in range(8):
        step = 2**(7-i)
        signal = tobinary(value + step)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        if (GPIO.input(comp) == 0):
            value += step
    return value
try:
    voltage = 0.0
    list_voltage = []
    list_t = []
    GPIO.output(troyka, 1)
    time_start = time.time()
    while voltage < 2.6683593749999996:
        value = adc()
        list_voltage.append(value)
        voltage = value/levels*maxvoltage
        time_finish = time.time()
        list_t.append(time_finish - time_start)
    

    GPIO.output(troyka, 0)
    while voltage > 2.6683593749999996:
        value = adc()
        list_voltage.append(value)
        voltage = value/levels*maxvoltage
        time_finish = time.time()
        list_t.append(time_finish - time_start)

    print(list_voltage, list_t)
    with open('data.txt', 'w') as f:
        for i in range(len(list_voltage)):
            f.write(str(list_voltage[i]) + '\n')
    
    discr = len(list_voltage)/(time_finish - time_start)
    qv = 3.3/256
    print(discr)
    with open('settings.txt', 'w') as settings:
        settings.write('frequency: ' + str(discr) + '\n')
        settings.write(str(qv))

    plt.plot(list_t, list_voltage)
    plt.xlabel('time, sec')
    plt.ylabel('voltage, V')
    plt.grid()
    plt.show()
    

    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

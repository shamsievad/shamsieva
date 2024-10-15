import RPi.GPIO as GPIO
import time
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
    while True:
        value = adc()
        voltage = value/levels*maxvoltage
        print(value, voltage)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
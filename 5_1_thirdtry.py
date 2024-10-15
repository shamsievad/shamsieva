import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
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
    for i in range(256):
        b = tobinary(i)
        GPIO.output(dac, b)
        time.sleep(0.01)
        if (GPIO.input(comp) == 1):
            return i
try:
    while True:
        vol = adc()
        voltage = float(vol)/256*3.3
        print(vol, voltage)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
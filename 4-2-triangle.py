import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def tobinary(n):
    a, a2 = [], []
    while len(a) != 8:
        a.append(n%2)
        n //= 2
    a2 = a[::-1]
    return a2
try:
    t = float(input())
    while True:        
        for i in range(256):
            b = tobinary(i)
            GPIO.output(dac, b)
            time.sleep(t/512)
         
        for i in range(254, -1, -1):
            b = tobinary(i)
            GPIO.output(dac, b)
            time.sleep(t/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

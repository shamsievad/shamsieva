import RPi.GPIO as GPIO
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
    while True:
        n = int(input())
        if ((n >= 0) and (n <= 255)):
            print('Voltage: ', 0.013*n)
            c = tobinary(n)
            GPIO.output(dac, c)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
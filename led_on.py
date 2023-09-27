import RPi.GPIO as GPIO
from time import sleep
dac = [8, 11, 7, 1,0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        x = 255
        for i in range(x):
            GPIO.output(dac, d2b(i))
            sleep(1)
        i -= 2
        while i > 0:
            GPIO.output(dac, d2b(i))
            sleep(1)
            i -= 1
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()

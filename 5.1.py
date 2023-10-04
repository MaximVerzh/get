import RPi.GPIO as GPIO
from time import sleep
dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = len(dac)
levels = 2**bits
comp = 14
troyka = 13
maxv = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


    
def adc():
    for i in range(256):
        GPIO.output(dac, d2b(i))
        sleep(0.001)
        compVal = GPIO.input(comp)
        if compVal != 0:
            return i
    return 255
    
        
try: 
    while (1):
        
        print(round((adc() / 256) * maxv, 2), "B")

       

       
        
finally:
    GPIO.output(dac + [troyka],0)
    GPIO.cleanup()

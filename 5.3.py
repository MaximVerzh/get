import RPi.GPIO as GPIO
from time import sleep
dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2,3, 4, 17, 27, 22, 10, 9]
bits = len(dac)
levels = 2**bits
comp = 14
troyka = 13
maxv = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + led,  GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


    
def adc():
    arr = [0]*8
    for i in range(8):
        arr[i] += 1
        GPIO.output(dac, arr)
        sleep(0.1)
        compVal = GPIO.input(comp)
        if compVal:
            arr[i] -= 1
    q = 0
    for i in range(8):
        q += arr[7-i] * 2 ** i
    return q
    
        
try: 
    while (1):
        value = adc()
        for i in range(8):
            if (value + 1) / 256 < (i + 1) / 8:
                GPIO.output(led[i], 0)
            else:
                GPIO.output(led[i], 1)

       

       
        
finally:
    GPIO.output(dac + [troyka] + led,0)
    GPIO.cleanup()

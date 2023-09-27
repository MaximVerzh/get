import RPi.GPIO as GPIO
from time import sleep
dac = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
val = 0
t = 3
step = 1
try:
    pwm0 = GPIO.PWM(21, 1000)
    pwm1 = GPIO.PWM(22, 1000)
    pwm0.start(0)
    pwm1.start(0)
    while True:
        x = int(input())
        

        
        
        print(3.3*(x/100))
        pwm0.ChangeDutyCycle(x)
        pwm1.ChangeDutyCycle(x)
    pwm0.stop()
    pwm1.stop()

       

       
        
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()

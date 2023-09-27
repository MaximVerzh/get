import RPi.GPIO as GPIO
from time import sleep
dac = [8, 11, 7, 1,0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while 1 > 0:
        x = int(input())
        GPIO.output(dac, d2b(x))
        print("V = " + str((round(3.3/256*x, 2))))
except RuntimeError:
    print("ввода значения превышающего возможности 8-разрядного ЦАП")
except ValueError:
    print("ввод не числового значения или ввод не целого числа или ввод отрицательного значения")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
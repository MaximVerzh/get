import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(24, GPIO.OUT)

GPIO.output(24, GPIO.HIGH)

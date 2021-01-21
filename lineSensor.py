import RPi.GPIO as GPIO

in=6 #Input pin for the yellow wire on the linefinder is GPIO pin 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(in, GPIO.IN)

def readSensor():
    return GPIO.input(in)


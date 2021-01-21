import RPi.GPIO as GPIO

def readSensor():
    in=6 #Input pin for the yellow wire on the linefinder is GPIO pin 6

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in, GPIO.IN)

    return GPIO.input(in)


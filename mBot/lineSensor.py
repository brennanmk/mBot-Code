import RPi.GPIO as GPIO

in1=6 #Input pin for the yellow wire on the linefinder is GPIO pin 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.IN)

def readSensor():
    return GPIO.input(in1)


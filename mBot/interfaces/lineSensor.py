import RPi.GPIO as GPIO

sensor_pin = -1
def init(pin):
    sensor_pin = pin

def read():
    return GPIO.input(sensor_pin)
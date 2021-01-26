import RPi.GPIO as GPIO

sensor_pin = -1

def init(pin):
    global sensor_pin
    sensor_pin = pin
    GPIO.setup(pin, GPIO.IN)
    
def read():
    return GPIO.input(sensor_pin)

import RPi.GPIO as GPIO

class LineSensor:

    def __init__(self,pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
    
    def read(self):
        return GPIO.input(self.pin)
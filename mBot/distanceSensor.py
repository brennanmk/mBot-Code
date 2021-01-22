import RPi.GPIO as GPIO
import time

class DistanceSensor:

    def __init__(self,trig,echo):
        self.trig = trig
        self.echo = echo
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.output(self.trig,0)
    
    def read_cm(self):
        GPIO.output(self.trig,1)
        time.sleep(0.0001)
        GPIO.output(self.trig,0)

        # Wait for pulse
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()

        # Returns distance in CM
        return round((pulse_end - pulse_start)*17150,2)
    
    def read_in(self):
        return self.read_cm() * 0.3937008
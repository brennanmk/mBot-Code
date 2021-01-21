import RPi.GPIO as GPIO

class Motor:

    def __init__(self,pEn,p1,p2):

        # Define pins
        self.pin_enable = pEn
        self.pin_dirA = p1
        self.pin_dirB = p2

        # Setup pinout
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_enable,GPIO.OUT)
        GPIO.setup(self.pin_dirA,GPIO.OUT)
        GPIO.setup(self.pin_dirB,GPIO.OUT)

        # Setup motor outputs
        GPIO.output(self.pin_dirA,GPIO.LOW)
        GPIO.output(self.pin_dirB,GPIO.LOW)

        self.pwm=GPIO.PWM(self.pin_enable,1000)
        self.pwm.start(0)
    
    # Write speed to motor
    def write(self,spd):
        spd = min(100,max(spd,-100))
        self.pwm.ChangeDutyCycle(abs(spd))
        # Change direction
        GPIO.output(self.pin_dirA,GPIO.LOW if spd < 0 else GPIO.HIGH)
        GPIO.output(self.pin_dirB,GPIO.LOW if spd > 0 else GPIO.HIGH)
    
    def stop(self):
        self.pwm.stop()
        GPIO.output(self.pin_dirA,GPIO.LOW)
        GPIO.output(self.pin_dirB,GPIO.LOW)

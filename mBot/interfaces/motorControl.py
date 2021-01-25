import RPi.GPIO as GPIO          
from time import sleep

#in Declarations for Motor1
in1 = 24
in2 = 23
en1 = 25

#Pin Declarations for Motor2
in3=22
in4=27
en2=17

#Motor1 Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en1,1000)
p.start(25)

#Motor2 Setup
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(en2,1000)
p.start(25)

def motorControl(value):
    #Control the motor based on the value entered (0 stop, 1 forward, 2 backward, 3 left, 4 right)
    if value==1:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)


    elif value==0:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

    elif value==2:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

    elif value==3:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)

    elif value==4:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

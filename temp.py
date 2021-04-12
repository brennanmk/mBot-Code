import robot.robot as robot
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
robot.init()
import time
robot.setLed(True)
time.sleep(5)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,False)

robot.cleanup()
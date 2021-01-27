# This file contains all the critical robot handling code
import RPi.GPIO as GPIO
import time

MOTOR_NAMES = ('LEFT','RIGHT')

def init():
    GPIO.setmode(GPIO.BCM)

def getLineSensor()
    return True

def getDistanceCM():
    return 0

def getDistanceIN():
    return getDistanceCM() * 0.3937008

def setMotorPower(motor,power):
    # Validate inputs
    power = min(100,max(power,-100))
    if motor not in MOTOR_NAMES:
        return
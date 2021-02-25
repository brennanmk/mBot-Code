# This file contains all the critical robot handling code
ON_PI = True
try:
    import RPi.GPIO as GPIO
except ImportError:
    ON_PI = False
import time
import robot.bot_config as config

MOTOR_NAMES = ('LEFT', 'RIGHT')

motor_pwm = {}
override_power = 50

pulse_start = 0
pulse_end = 0

def init():
    if ON_PI:
        GPIO.setmode(GPIO.BCM)
        # Setup line sensor
        GPIO.setup(config.PINS['line/sense'], GPIO.IN)
        # Setup ultrasonic sensor
        GPIO.setup(config.PINS['ultrasonic/trig'], GPIO.OUT)
        GPIO.setup(config.PINS['ultrasonic/echo'], GPIO.IN)
        GPIO.output(config.PINS['ultrasonic/trig'], 0)
        # Setup motors
        for name in MOTOR_NAMES:
            setupMotor(name.lower())
        # Give the US sensor time to denoise
        time.sleep(1)


def setupMotor(name):
    name = 'motor_'+name
    GPIO.setup(config.PINS[name+'/dira'], GPIO.OUT)
    GPIO.setup(config.PINS[name+'/dirb'], GPIO.OUT)
    GPIO.setup(config.PINS[name+'/en'], GPIO.OUT)
    motor_pwm[name] = GPIO.PWM(config.PINS[name+'/en'], 1000)
    # Set defaults
    GPIO.output(config.PINS[name+'/dira'], 0)
    GPIO.output(config.PINS[name+'/dirb'], 0)
    motor_pwm[name].start(0)


def getLineSensor():
    if ON_PI:
        return GPIO.input(config.PINS['line/sense'])
    else:
        return 0

def getLeftMotorPower():
    return config.PINS['motor_power/left']

def getRightMotorPower():
        return config.PINS['motor_power/right']
    
def getDistanceCM():
    global pulse_start
    global pulse_end
    if ON_PI:
        pin_trigger = config.PINS['ultrasonic/trig']
        pin_echo = config.PINS['ultrasonic/echo']

        GPIO.output(pin_trigger, 1)
        time.sleep(0.0001)
        GPIO.output(pin_trigger, 0)

        timeout_start = time.time()

        # Wait for pulse
        while GPIO.input(pin_echo) == 0:
            pulse_start = time.time()
            if pulse_start - timeout_start > 1:
                print("ERROR: Ultrasonic sensor timed out")
                return -1
        while GPIO.input(pin_echo) == 1:
            pulse_end = time.time()
            if pulse_end - timeout_start > 1:
                print("ERROR: Ultrasonic sensor timed out")
                return -1
        # Returns distance in CM
        return round((pulse_end - pulse_start)*17150, 2)
    else:
        return -1


def getDistanceIN():
    return round(getDistanceCM() * 0.3937008, 2)

def setLed(state):
    GPIO.output(config.PINS['misc/led'],1 if state else 0)

def drive(dir):
    setMotorPower('left',override_power*dir)
    setMotorPower('right',override_power*dir)

def turn(dir):
    setMotorPower('left',override_power*-dir)
    setMotorPower('right',override_power*dir)

def stop():
    setMotorPower('left',0)
    setMotorPower('right',0)

def setMotorPower(motor, power):
    if ON_PI:
        # Validate inputs

        name = 'motor_'+motor.lower()
        GPIO.output(config.PINS[name+'/dira'], power > 0)
        GPIO.output(config.PINS[name+'/dirb'], power < 0)
        motor_pwm[name].ChangeDutyCycle(abs(power))

# Cleanup robot


def cleanup():
    if ON_PI:
        for name in MOTOR_NAMES:
            setMotorPower(name, 0)
            motor_pwm['motor_'+name.lower()].stop()


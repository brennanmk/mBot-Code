# This file contains the robot handling code
ON_PI = True #Check to see if the code is being executed on raspberry pi or on another device
try:
    import RPi.GPIO as GPIO
except ImportError:
    ON_PI = False
import time
import robot.bot_config as config

#Variable Initilization
MOTOR_NAMES = ('LEFT', 'RIGHT')

motor_pwm = {}
override_power = 100
motor_tilt = 0

pulse_start = 0
pulse_end = 0

def init(): #Function used to initialize the motor GPIO

    #Read the the config file to get speed and motor tilt values
    override_power = config.MOTOR['speed']
    motor_tilt = config.MOTOR['tilt']

    #Check to see if on raspberry pi and if so initalize the GPIO pins are specified in pins.ini
    if ON_PI:
        GPIO.setmode(GPIO.BCM)
        # Setup line sensor
        GPIO.setup(config.PINS['line/sense'], GPIO.IN)
        # Setup ultrasonic sensor
        GPIO.setup(config.PINS['ultrasonic/trig'], GPIO.OUT)
        GPIO.setup(config.PINS['ultrasonic/echo'], GPIO.IN)
        GPIO.output(config.PINS['ultrasonic/trig'], 0)
        # Setup LED
        GPIO.setup(config.PINS['misc/led'], GPIO.OUT)
        # Setup motors
        for name in MOTOR_NAMES:
            setupMotor(name.lower())
        # Give the US sensor time to denoise
        time.sleep(1)


def setupMotor(name): #Function to setup the GPIO pins for the motors
    name = 'motor_'+name
    # Parse values from pins.ini and initalize the specified GPIO pins
    GPIO.setup(config.PINS[name+'/dira'], GPIO.OUT)
    GPIO.setup(config.PINS[name+'/dirb'], GPIO.OUT)
    GPIO.setup(config.PINS[name+'/en'], GPIO.OUT)
    motor_pwm[name] = GPIO.PWM(config.PINS[name+'/en'], 1000)
    # Set defaults
    GPIO.output(config.PINS[name+'/dira'], 0)
    GPIO.output(config.PINS[name+'/dirb'], 0)
    motor_pwm[name].start(0)


def getLineSensor(): #Function to return the value of the line sensor
    #If on pi read the input from the line sensor GPIO pin as specified in pins.ini
    if ON_PI:
        return GPIO.input(config.PINS['line/sense'])
    else:
        return 0

def getMotorSpeed(): #Function to check the motor speed
    return override_power

def getMotorTilt(): #Function to check the motor tilt
    return motor_tilt
    
def getDistanceCM(): # Function to return the value of the ultrasonic sensor
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


def getDistanceIN(): #Function to convert the distance sensor value from CM to IN
    return round(getDistanceCM() * 0.3937008, 2)

def setLed(state): #Function to change the state of the LED
    #Check the pins.ini file for an LED and then switch its state
    GPIO.output(config.PINS['misc/led'],1 if state else 0)

def drive(dir): #Function to have the bot drive in a specfied direction
    #Use the set motor power funtions to drive the bot in the specified direction
    setMotorPower('LEFT',override_power*dir * (1-max(0,-motor_tilt)))
    setMotorPower('RIGHT',override_power*dir * (1-max(0,motor_tilt)))

def turn(dir): #Function to have the bot turn in a specfied direction
    #Use the set motor power funtions to turn the bot in the specified direction
    setMotorPower('LEFT',override_power*-dir * (1-max(0,-motor_tilt)))
    setMotorPower('RIGHT',override_power*dir * (1-max(0,motor_tilt)))

def stop(): #Function to have the stop the bot
    #Use the set motor power functions to stop each motor
    setMotorPower('LEFT',0)
    setMotorPower('RIGHT',0)

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


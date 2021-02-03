# This file contains all the critical robot handling code
import RPi.GPIO as GPIO
import time
try:
    import robot.bot_config as config
except ImportError:
    try:
        import bot_config as config
    except ImportError:
        print("Cannot find config!")

MOTOR_NAMES = ('LEFT', 'RIGHT')

motor_pwm = {}


def init():
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
    GPIO.setup(config.PINS[name+'/pwm'], GPIO.OUT)
    motor_pwm[name] = GPIO.PWM(config.PINS[name+'/pwm'], 1000)
    # Set defaults
    GPIO.output(config.PINS[name+'/dira'], 0)
    GPIO.output(config.PINS[name+'/dirb'], 0)
    motor_pwm[name].start(0)


def getLineSensor():
    return GPIO.input(config.PINS['line/sense'])


def getDistanceCM():

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


def getDistanceIN():
    return round(getDistanceCM() * 0.3937008, 2)

def setLed(state):
    GPIO.output(config.PINS['misc/led'],1 if state else 0)

def setMotorPower(motor, power):
    # Validate inputs
    power = min(100, max(power, -100))
    if motor not in MOTOR_NAMES:
        return

    name = 'motor_'+motor.lower()
    GPIO.output(config.PINS[name+'/dira'], power > 0)
    GPIO.output(config.PINS[name+'/dirb'], power < 0)
    motor_pwm[name].ChangeDutyCycle(abs(power))

# Cleanup robot


def cleanup():
    for name in MOTOR_NAMES:
        name = 'motor_'+name.lower()
        setMotorPower(name, 0)
        motor_pwm[name].stop()
    GPIO.cleanup()

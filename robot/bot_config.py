import configparser

DEFAULT_CONFIG = {
    'motor_right':{
        'pwm':12,
        'dirA':16,
        'dirB':20
    },
    'motor_left':{
        'pwm':19,
        'dirA':13,
        'dirB':6
    },
    'ultrasonic':{
        'trig':23,
        'echo':24
    },
    'line':{
        'sense':21
    },
    'motor_config':{
        'trim':0.0,
        'speed':100
    }
}

#NOTE: PINS ARE STORED IN BCM MODE
PINS = {}
MOTOR = {'speed':100,'tilt':0}

def load_config():
    print("Loading config from file...")
    cfg = configparser.ConfigParser()

    # Look for file
    if not cfg.read('pins.ini'):
        print('Bot config file missing, generating from defaults')
        # Copy defaults
        for section in DEFAULT_CONFIG:
            cfg[section] = {}
            for item in DEFAULT_CONFIG[section]:
                cfg[section][item] = str(DEFAULT_CONFIG[section][item])
        # Write to file
        with open('pins.ini','w') as file:
            cfg.write(file)

    
    # Iterate over INI file and read data
    for section in cfg.sections():
        if section != 'motor_config':
            for item in cfg[section]:

                path = section+"/"+item
                # Ensure the pin is a number
                try:
                    index = int(cfg[section][item])
                except ValueError:
                    print("ERROR: Bad pin value @ '",path,"'")
                    continue

                # Ensure the pin is PWM 
                if item.find("pwm") == 0 and not pin_is_pwm(index):
                    print("ERROR: Pin",index,"at path '",index,"' is not a PWM pin")
                else:
                    # Load em
                    PINS[path] = index
    
    # Load motor data
    MOTOR['speed'] = cfg['motor_config'].getint('speed')
    MOTOR['tilt'] = cfg['motor_config'].getfloat('tilt')

    # Confirm load
    print("Done, found",len(PINS),"pins")

# Check if a pin is a PWM pin
def pin_is_pwm(pin):
    return pin in (18,12,19,13)

load_config()

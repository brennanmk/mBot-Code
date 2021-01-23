import configparser

DEFAULT_PINS = {
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
        'trigger':23,
        'echo':24
    },
    'line':{
        'sense':21
    }
}

#NOTE: PINS ARE STORED IN BCM MODE
PINS = {}

def load_pin_config():
    print("Loading pins from file...")
    pin_cfg = configparser.ConfigParser()

    # Look for file
    if not pin_cfg.read('mBot/pins.ini'):
        print('Bot config file missing, generating from defaults')
        # Copy defaults
        for section in DEFAULT_PINS:
            pin_cfg[section] = {}
            for item in DEFAULT_PINS[section]:
                pin_cfg[section][item] = str(DEFAULT_PINS[section][item])
        # Write to file
        with open('mBot/pins.ini','w') as file:
            pin_cfg.write(file)

    
    # Iterate over INI file and read data
    for section in pin_cfg.sections():
        for item in pin_cfg[section]:

            pin_path = section+"/"+item
            # Ensure the pin is a number
            try:
                pin_index = int(pin_cfg[section][item])
            except ValueError:
                print("ERROR: Bad pin value @ '",pin_path,"'")
                continue

            if pin_index < 1 or pin_index > 27:
                print("ERROR: Pin ",pin_index,"at path '",pin_path,"' is out of range")
            
            # Ensure the pin is PWM 
            if item.find("pwm") == 0 and not pin_is_pwm(pin_index):
                print("ERROR: Pin",pin_index,"at path '",pin_path,"' is not a PWM pin")
            else:
                # Load em
                PINS[pin_path] = pin_index
    # Confirm load
    print("Done, found",len(PINS),"pins")

# Check if a pin is a PWM pin
def pin_is_pwm(pin):
    return pin in (18,12,19,13)


load_pin_config()

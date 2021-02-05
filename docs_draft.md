# WitBot Reference

## Raspberry Pi Zero
### Pins
The WitBot is powered by a Raspberry Pi Zero W, which uses a section of pins called 'GPIO' (**G**eneral **P**urpose **I**nput and **O**utput). 

Each of these pins has 2 numbers used to refer to it:
- A **Board** number, indicated on the chart below by the number in the circle. Every pin has one of these. This numbering system is *not* used by the Blockly interface or pin definition file.
- A **BCM** number, indicated by the rectangle next to the circle on the chart below. For instance, a pin labeled `GPIO14` has BCM pin number 14. Unlike board pins, only pins which can be used for GPIO have these - so, power pins are left out. The WitBot uses these to refer to pins.

![Raspberry Pi Zero Pinout](/static/img/pinout.png)

*(Source: TODO find source of image)*

If you want to edit the pins your robot uses, bear in mind the distinction between BCM and Board pins. The pin definitions themselves are located in the `pins.ini` file, and can be edited with any plain old text editor.
The default pins are:
```
[motor_right]
pwm = 12
dira = 24
dirb = 23

[motor_left]
pwm = 13
dira = 22
dirb = 27

[ultrasonic]
trig = 26
echo = 19

[line]
sense = 6

[misc]
led = 2
```

## Troubleshooting
### Ultrasonic sensor
The ultrasonic sensor will usually be the easiest to find problems with. If the readout on the control panel says 'Timeoutcm', it means something is wrong

Typically, the issue is caused by one of the following problems, in order from least to most hard to repair:
- The pins on the ultrasonic sensor are wired incorrectly. Check the pins above and make sure your wiring is right
- The resistor circuit is wired incorrectly. Check the setup guide to make sure everything is in place
- The pins used on the pi are burnt out or broken - try changing the pins in the config file and the circuit
- The sensor itself is broken, and needs to be replaced

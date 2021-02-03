# this script runs as soon as the robot turns on
# make sure to add this to rc.local
import robot
import time
import os

# Check for ip_info.txt file
if os.path.isfile('/boot/ip_info.txt'):
	# We're good
	blink(3)

	# Start main robot code from here
else:
	# Find IP
	import socket
	ip_addr = socket.gethostbyname(socket.gethostname())
	with (open('/boot/ip_info.txt','w')) as f:
		f.write(ip_addr+":5000")

	blink(5)

	# Shutdown
	import subprocess
	subprocess.call("sudo shutdown -h now",shell=True)

# Used to blink the LED
def blink(count):
	for i in range(count):
		robot.setLed(True)
		time.sleep(0.25)
		robot.setLed(False)
		time.sleep(0.25)
import robot.robot as robot
robot.init()
import time
for count in range(10):
  robot.setMotorPower("LEFT",-100)
  robot.setMotorPower("RIGHT",100)
  time.sleep(1)

robot.cleanup()
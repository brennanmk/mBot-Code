import robot.robot as robot
robot.init()
import time
robot.setMotorPower("LEFT",100)
robot.setMotorPower("RIGHT",100)
time.sleep(10)

robot.cleanup()
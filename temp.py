import robot.robot as robot
robot.init()
import time
robot.setMotorPower("RIGHT",25)
robot.setMotorPower("LEFT",100)
time.sleep(5)

robot.cleanup()
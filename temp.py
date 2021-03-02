import robot.robot as robot
robot.init()
import time
robot.drive(-1)
time.sleep(5)
robot.stop()

robot.cleanup()
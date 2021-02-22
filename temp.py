import robot.robot as robot
robot.init()
import time
robot.turn(-1)
time.sleep(5)
robot.stop()

robot.cleanup()
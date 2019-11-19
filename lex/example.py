import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()


cozmo.run_program(cozmo_program)
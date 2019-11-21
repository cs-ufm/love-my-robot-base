import cozmo
from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
from cozmo.util import degrees, distance_mm, radians, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text('HI').wait_for_completed()
    robot.say_text('HELLO').wait_for_completed()
cozmo.run_program(cozmo_program)

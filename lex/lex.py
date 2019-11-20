import asyncio
import sys
import cozmo
from flask import Flask

from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
from cozmo.util import degrees, distance_mm, radians, speed_mmps

app = Flask(__name__)

#Cozmo functions
def sayhello(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()

def move(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

def moveback(robot: cozmo.robot.Robot):
    # Drive backwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(-150), speed_mmps(50)).wait_for_completed()

def turn(robot: cozmo.robot.Robot):
    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(90)).wait_for_completed()



@app.route("/e")
def index():
    return "Hello from Python!"

@app.route('/')
def hello_world():
    cozmo.run_program(moveback)

    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
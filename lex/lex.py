import asyncio
import sys
import cozmo
import time
from flask import Flask

from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
from cozmo.util import degrees, distance_mm, radians, speed_mmps

app = Flask(__name__)

#Cozmo functions
async def sayhello(robot: cozmo.robot.Robot):
    async with robot.perform_off_charger():
        action = robot.say_text("Hello World")
        await action.wait_for_completed()

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

def lift(robot: cozmo.robot.Robot):
    # Tell the head motor to start lowering the head (at 5 radians per second)
    #robot.move_head(-5)
    # Tell the lift motor to start lowering the lift (at 5 radians per second)
    robot.move_lift(-5)
    # Tell Cozmo to drive the left wheel at 25 mmps (millimeters per second),
    # and the right wheel at 50 mmps (so Cozmo will drive Forwards while also
    # turning to the left
    #robot.drive_wheels(25, 50)

#Animations
def celebration(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()  

def Hiccup(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()  



#Animals
def duck(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDuck).wait_for_completed()    

def Elephant(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabElephant).wait_for_completed()  



@app.route("/e")
def index():
    return "Hello from Python!"

@app.route('/')
def hello_world():
    cozmo.run_program(Elephant)

    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
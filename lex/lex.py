
from flask import Flask,render_template
import json

app = Flask(__name__)
from datetime import datetime
import os

robot = cozmo.robot.Robot
measures = cozmo.util
def cozmo_say(robot: cozmo.robot.Robot):
    robot.say_text("Hello Flask").wait_for_completed()

def cozmo_turn(robot: cozmo.robot.Robot, accel, angle, speed):
    robot.turn_in_place(angle, speed, accel).wait_for_completed()

def cozmo_move(robot: cozmo.robot.Robot, distance, speed, should_play_anim=None):
    robot.drive_straight(distance, speed, should_play_anim)

def cozmo_off(robot: cozmo.robot.Robot, parallel=False, num_retries=1):
    robot.drive_off_charger_contacts(parallel, num_retries)

def cozmo_pick(robot: cozmo.robot.Robot, obj, in_parallel, num_retries=1):
    robot.pickup_object(obj, in_parallel, num_retries)

def command_center_drive(funct, arg1=None, arg2=None, arg3=None):
    cozmo.run_program(drive[funct](arg1,arg2,arg3))

def generate_code(test):
    truename = datetime.now().minute
    with open('transpiled/cozmo_generated_program.py', 'w') as f:
<<<<<<< HEAD
        f.write('import datetime \nimport cozmo\nfrom cozmo.util import degrees\n'+test+'\n')
=======
        f.write('import datetime \nimport cozmo\nclass transpiled:\n\n  def __init__(self, robot: cozmo.robot.Robot, cube: cozmo.objects.LightCube):\n      self.robot = robot\n      self.cube = cube\n\n  def cozmo_program(self, robot: cozmo.robot.Robot):\n      measure = cozmo.util\n'+test+'\n  def run(self):\n      cozmo.run_program(self.cozmo_program)\nCOZMO = transpiled(cozmo.robot.Robot, cozmo.objects.LightCube)\nCOZMO.run()')
>>>>>>> a34b780d0274071f62f5aef8003bf632bfbbdc84

    #import cozmo_generated_program as p
    
    os.rename(r'transpiled/cozmo_generated_program.py', r'transpiled/cozmo_generated_program'+str(truename)+r'.py')


#revisar COZMO.UTIL para sacar medidas y datos
drive  = {
    'SAY': '      robot.say_text({}).wait_for_completed()',
    'TURN': '      robot.turn_in_place(measure.degrees({}), measure.Speed({})).wait_for_completed()',
    'PICK': '      robot.drive_off_charger_contacts()',
    'DRIVE': '      robot.drive_straight(measure.distance_mm({}), measure.Speed({})).wait_for_completed()',
<<<<<<< HEAD
    'DRIVE_OFF': cozmo_off,
=======
<<<<<<< HEAD
    'DRIVE_OFF': "async def roll_a_cube(robot: cozmo.robot.Robot):\n" +
"    await robot.set_head_angle(degrees({})).wait_for_completed()\n" +
"    print(\"Cozmo is waiting until he sees a cube\")\n" +
"    cube = await robot.world.wait_for_observed_light_cube()\n" +
"    print(\"Cozmo found a cube, and will now attempt to roll with it:\")\n" +
"    # Cozmo will approach the cube he has seen and roll it\n" +
"    # check_for_object_on_top=True enforces that Cozmo will not roll cubes with anything on top\n" +
"    action = robot.roll_cube(cube, check_for_object_on_top=True, num_retries=2)\n" +
"    await action.wait_for_completed()\n" +
"    print(\"result:\", action.result)\n" +
"cozmo.run_program(roll_a_cube)\n",
    'ROLL_CUBE': 'async def roll_a_cube(robot: cozmo.robot.Robot):\n    await robot.set_head_angle(degrees(-5.0)).wait_for_completed()\n    print("Cozmo is waiting until he sees a cube")\n    cube = await robot.world.wait_for_observed_light_cube()\n    print("Cozmo found a cube, and will now attempt to roll with it:")\n    action = robot.roll_cube(cube, check_for_object_on_top=True, num_retries=2)\n    await action.wait_for_completed()\n    print("result:", action.result)\ncozmo.run_program(roll_a_cube)'
=======
    'DRIVE_OFF': cozmo_off
>>>>>>> a3d8b528f9e344bf09e2dd190b56790aa30a4b7d
    'ROLL_CUBE': 'async def roll_a_cube(robot: cozmo.robot.Robot):\n    await robot.set_head_angle(degrees(-5.0)).wait_for_completed()\n    print("Cozmo is waiting until he sees a cube")\n    '
>>>>>>> a34b780d0274071f62f5aef8003bf632bfbbdc84
}
arg1 ='"HELLO FLASK"'
'''@app.route('/')
def hello_world():
    cozmo.run_program(cozmo_program)

<<<<<<< HEAD
    return render_template("index.html")'''



=======
    return 'Hello, World!'''
<<<<<<< HEAD


#if __name__ == "__main__":
 #   app.run(host="0.0.0.0")

generate_code(drive['DRIVE_OFF'].format('69.0'))
=======
>>>>>>> a34b780d0274071f62f5aef8003bf632bfbbdc84
>>>>>>> a3d8b528f9e344bf09e2dd190b56790aa30a4b7d

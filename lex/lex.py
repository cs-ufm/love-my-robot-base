import redis, json, threading, time, asyncio, os, cozmo, sys
from flask import Flask
from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
from cozmo.util import degrees, distance_mm, radians, speed_mmps
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

app = Flask(__name__)
r = redis.StrictRedis(host="localhost", port=6379, db=0)
#cmmnt here
p = r.pubsub(ignore_subscribe_messages=True)
channel = 'do'
global_json = None
robot= cozmo.robot.Robot
python_file = "test1.py"

def isNumber(maybe_number):
    return isinstance(maybe_number, int) or isinstance(maybe_number, float)

# #Cozmo functions
''' Move functions
    -lift
    -moveforward
    -movebackward
    -turn
'''

def sayhello(string_to_say):
    return f"    robot.say_text('{string_to_say}').wait_for_completed()"

def lift(numbertolift):
    float(numbertolift)
    return f"    robot.move_lift({numbertolift})"

def move(distance_speed):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    #robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    params_list = distance_speed.split(" ")
    if len(params_list) == 2:
        param1 = float(params_list[0])
        param2 = float(params_list[1])
    else:
        param1 = 150
        param2 = 50
    return f"    robot.drive_straight(distance_mm({param1}), speed_mmps({param2})).wait_for_completed()"

def moveback(negativedistance_speed):
    # Drive backwards for 150 millimeters at 50 millimeters-per-second.
    params_list = negativedistance_speed.split(" ")
    if len(params_list) == 2:
        param1 = float(params_list[0])
        param2 = float(params_list[1])
    else:
        param1 = -150
        param2 = 50
    return f"    robot.drive_straight(distance_mm({param1}), speed_mmps({param2})).wait_for_completed()"

def turn(degrees):
    int(degrees)
    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    return f"    robot.turn_in_place(degrees({degrees})).wait_for_completed()"

#def tap(robot: cozmo.robot.Robot):
        # Move the lift to the top, and wait for it to get there
 #       robot.set_lift_height(1).wait_for_completed()
        # Move the lift down fairly quickly for 0.1 seconds
#	robot.move_lift(-3.5)
#	time.sleep(0.1)
        # Move the lift back to the top quickly, and wait for it to get there
#	robot.set_lift_height(1, accel=20, max_speed=20).wait_for_completed()

def print_Name(robot: cozmo.robot.Robot):
    name = input('What’s your name ? ')
    print(“Hello {}”.format(name)    
          
def celebration(action):
    return f"    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLab+'{action}'+).wait_for_completed()"     

def message_handler(message):
    """Converts message string to JSON.

    Once invoked through asyncSUB() it handles
    the message by converting it from string
    to JSON and assigns it to 'global_json'
    """
    print(f"MY HANDLER: '{message.get('data')}")
    json_message = None
    message_data = message.get('data')

    if message_data:
        json_message = json.loads(message_data) # converts to JSON type
        function_getter_from_JSON(json_message)
        global_json = json_message
        

LMR_to_func_dict = {
     "SAY" : sayhello,
     "LIFT": lift,
     "MOVE": move,
     "MOVEBACK": moveback,
     "TURN": turn,
     "WIN": celebration

 }

def function_getter_from_JSON(JSON):
    """Receives a JSON and extractrs the LMR
    function and param and passes it as string.

    Do desc later.
    """
    functions_and_params = []
    functions_and_params = JSON.get('lmr')
    f = open(python_file, "w")
    f.write("import cozmo\n")
    f.write("from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light\n")
    f.write("from cozmo.util import degrees, distance_mm, radians, speed_mmps\n")
    f.write("def cozmo_program(robot: cozmo.robot.Robot):\n")
        
    for eachFuncParam in functions_and_params:
        
        list_of_func_params = eachFuncParam.split(" ")
        str_func = list_of_func_params[0]
        function = LMR_to_func_dict.get(str_func)

        if len(list_of_func_params) == 1: # no param
            string_print = function()

        elif len(list_of_func_params) == 2: # one param
            str_param = list_of_func_params[1]

            if isNumber(str_param):
                string_print = function(f"{str_param}")
            else:
                string_print = function(f"'{str_param}'")


        elif len(list_of_func_params) == 3: # two params
            str_param1 = list_of_func_params[1]
            str_param2 = list_of_func_params[2]

            if isNumber(str_param1) and isNumber(str_param2):
                string_print = function(f"{str_param1},{str_param2}")
            else:
                string_print = function(f"'{str_param1}','{str_param2}'")

        f.write(f"{string_print}\n")

    f.write("cozmo.run_program(cozmo_program)\n")
    f.close()
    os.system(f"python3 {python_file}")


def asyncSUB():
    """Subscribes to channel and sends message 
    to handler.

    When in need of reading messages this is the 
    function to call. Once called it will subscribe 
    asynchronously to channel (where channel = 'CHANNEL_NAME' 
    defined on the first lines of this file).

    p.run_in_thread(): Behind the scenes, this is
    simply a wrapper around get_message() that runs 
    in a separate thread, and use asyncio.run_coroutine_threadsafe() 
    to run coroutines.

    Coroutine: Coroutines are generalization of subroutines. 
    They are used for cooperative multitasking where a process 
    voluntarily yields (give away) control periodically or when 
    idle in order to enable multiple applications to be run 
    simultaneously.
    """
    p.subscribe(**{channel: message_handler})
    thread = p.run_in_thread(sleep_time=0.1, daemon=True)
    message = p.get_message()
    print(f"asyncSUB: message: {message}")


#MOVE
# def moveback(robot: cozmo.robot.Robot):
#     # Drive backwards for 150 millimeters at 50 millimeters-per-second.
#     robot.drive_straight(distance_mm(-150), speed_mmps(50)).wait_for_completed()

#TURN
# def turn(robot: cozmo.robot.Robot):
#     # Turn 90 degrees to the left.
#     # Note: To turn to the right, just use a negative number.
#     robot.turn_in_place(degrees(90)).wait_for_completed()
 
#Animations
#Animations 5

def celebration(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()  
# def celebration(robot: cozmo.robot.Robot):
#     robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()  

def Hiccup(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHiccup).wait_for_completed()  

def Surprise(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSurprise).wait_for_completed()  

def Excited(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabExcited).wait_for_completed()  

def Sneeze(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSneeze).wait_for_completed()  

def Scared(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaredCozmo).wait_for_completed()  

#Animals
def duck(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDuck).wait_for_completed()    

def Elephant(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabElephant).wait_for_completed()  

# Soung

def sound():
    return f"    robot.play_audio(cozmo.audio.AudioEvents.SfxGameWin)\n    time.sleep(1.0)"

def sound80s():
    return f"    robot.play_audio(cozmo.audio.AudioEvents.MusicStyle80S1159BpmLoop)"

def soundStop():
    return f"    time.sleep(2.0)\n    robot.play_audio(cozmo.audio.AudioEvents.MusicStyle80S1159BpmLoopStop)"

# Lights

def cubeOneLights():
    return f'cube1 = robot.world.get_light_cube(LightCube1Id)\n if cube1 is not None:\n    cube1.set_lights(cozmo.lights.red_light)\n else:\n    cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")\n time.sleep(10)\n'

def cubeTwoLights():
    return f'cube2 = robot.world.get_light_cube(LightCube2Id)\n if cube2 is not None:\n    cube2.set_lights(cozmo.lights.green_light)\n else:\n    cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")\n time.sleep(10)\n'

def cubeThreeLights():
    return f'cube3 = robot.world.get_light_cube(LightCube3Id)\n if cube3 is not None:\n    cube3.set_lights(cozmo.lights.blue_light)\n else:\n    cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")\n time.sleep(10)\n'

if __name__ == "__main__":
    """We start asyncSUB() and Flask.

    We call the main function 'asyncSUB()' to subscribe asynchronously to 
    the channel; 
    this is were the fun begins.
    """
    asyncSUB()
    app.run(host="0.0.0.0")
    
    
@app.route('/')
def hello_world():
    cozmo.run_program(Elephant)



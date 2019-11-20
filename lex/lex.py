import redis, json, threading, time, asyncio, os, cozmo, sys
from flask import Flask
from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
from cozmo.util import degrees, distance_mm, radians, speed_mmps

app = Flask(__name__)
r = redis.StrictRedis(host="localhost", port=6379, db=0)
#cmmnt here
p = r.pubsub(ignore_subscribe_messages=True)
channel = 'do'
global_json = None
robot= cozmo.robot.Robot
python_file = "test1.py"
# #Cozmo functions
def sayhello(string_to_say):
    return f"    robot.say_text({string_to_say}).wait_for_completed()"

def lift(numbertolift):
    return f"    robot.move_lift({numbertolift})"

def move(distance, speed):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    #robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    return f"    robot.drive_straight(distance_mm({distance}), speed_mmps({speed}).wait_for_completed())"

def moveback(negativedistance, speed):
    # Drive backwards for 150 millimeters at 50 millimeters-per-second.
    return f"    robot.drive_straight(distance_mm({negativedistance}), speed_mmps({speed}).wait_for_completed())"
    
    

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
     "MOVEBACK": moveback

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
        
        str_func = eachFuncParam.split(" ")[0]
        str_param = eachFuncParam.split(" ")[1]

        function = LMR_to_func_dict.get(str_func)
        string_print = function(f"'{str_param}'")
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

def turn(robot: cozmo.robot.Robot):
    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(90)).wait_for_completed()



#Animations
def celebration(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed()  

def Hiccup(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHiccup).wait_for_completed()  

def Surprise(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSurprise).wait_for_completed()  


#Animals
def duck(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDuck).wait_for_completed()    

def Elephant(robot: cozmo.robot.Robot):
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabElephant).wait_for_completed()  


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




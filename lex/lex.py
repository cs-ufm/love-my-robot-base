
from flask import Flask,render_template
import json, sys

app = Flask(__name__)
from datetime import datetime
import os
sys.path.append('c:/Users/justf/LMR/love-my-robot-base/lex/transpiled')
#robot = cozmo.robot.Robot
#measures = cozmo.util

def generate_code(test, cond):
    timestamp = datetime.now().minute
    with open('transpiled/cozmo_generated_program.py', 'w') as f:
        if cond:
            f.write('import cozmo \nimport cozmo\nfrom cozmo.util import degrees, distance_mm, speed_mmps\nasync def cozmo_program(robot: cozmo.robot.Robot):\n    '+test+'\ndef run(cozmo_program):\n    cozmo.run_program(cozmo_program)')
        if not cond:
            f.write('import cozmo \nimport cozmo\nfrom cozmo.util import degrees, distance_mm, speed_mmps\ndef cozmo_program(robot: cozmo.robot.Robot):\n    '+test+'\ndef run(cozmo_program):\n    cozmo.run_program(cozmo_program)')
    import cozmo_generated_program as p
    #try:
        #p.run(p.cozmo_program)
    #except:
    #    print('DIDNT FINISH')
    os.rename(r'transpiled/cozmo_generated_program.py', r'transpiled/cozmo_generated_program'+str(timestamp)+r'.py')


#reading json file



#en el json falta poner los parámetros de cada funciones para leerlos y jalarlos
data = {
    'ROLL_CUBE': "await robot.set_head_angle(degrees(-5.0)).wait_for_completed()\n" +
"    print(\"Cozmo is waiting until he sees a cube\")\n" +
"    cube = await robot.world.wait_for_observed_light_cube()\n" +
"    print(\"Cozmo found a cube, and will now attempt to roll with it:\")\n" +
"    action = robot.roll_cube(cube, check_for_object_on_top=True, num_retries=2)\n" +
"    await action.wait_for_completed()\n" +
"    print(\"result:\", action.result)\n",
    'TEST': 'print("LA DE VICTOR")'
}
#revisar COZMO.UTIL para sacar medidas y datos
'''@app.route('/')
def hello_world():
    cozmo.run_program(cozmo_program)

    return render_template("index.html")'''

instrucciones = []
def leer_instrucciones(lista):
    for i in lista:
        instrucciones.append(i.split(' '))
    for x in instrucciones:
        try:
            print(x[0],x[1])
        except IndexError:
            print(x[0])

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0"
test = ['FALSE']
boolean = False
if test[0] == 'FALSE':
    boolean = True
generate_code(data['TEST'], boolean)

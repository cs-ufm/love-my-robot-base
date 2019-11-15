from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template ("index.html" , codigo_generado = codigo_generado)

codigo_generado = "import datetime \nimport cozmo\nclass transpiled:\n\n  def _init_(self, robot: cozmo.robot.Robot, cube: cozmo.objects.LightCube):\n      self.robot = robot\n      self.cube = cube\n\n  def cozmo_program(self, robot: cozmo.robot.Robot):\n      measure = cozmo.util\n+test+'\n  def run(self):\n      cozmo.run_program(self.cozmo_program)\nCOZMO = transpiled(cozmo.robot.Robot, cozmo.objects.LightCube)\nCOZMO.run()"

if __name__ == "__main__":
   app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import interfaces.motorControl as motorControl
import interfaces.lineSensor as lineSensor
import interfaces.distanceSensor as distanceSensor
import bot_config as config
import threading
import time

# Setup flask app
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
running = True

# Setup bot components
line = lineSensor.LineSensor(config.PINS['line/sense'])
lineValue = line.read()

distance = distanceSensor.DistanceSensor(config.PINS['ultrasonic/trigger'],config.PINS['ultrasonic/echo'])
distValue = distance.read_cm()

def updateSensor():
              global lineValue,distValue

              print('start of thread')
              while running: # global variable to stop loop
                            lineValue = line.read()
                            distValue = distance.read_cm()
                            time.sleep(1)
              print('stop of thread')
              
@app.route("/")
def indexRefresh(device=None, action=None):
              threading.Thread(target=updateSensor).start()
              return render_template('index.html',pinouts=config.PINS.keys())

@app.route("/", methods=['GET', 'POST'])
def index():
              if request.method == 'POST':
                            if request.form.get('Forward') == 'Forward':
                                          motorControl.motorControl(1)
                                          print("Motor Forward")
                            elif  request.form.get('Stop') == 'Stop':
                                          motorControl.motorControl(0)
                                          print("Motor Stop")
                            elif request.form.get('Backwards') == 'Backwards':
                                          motorControl.motorControl(2)
                                          print("Motor Back")
                            elif request.form.get("Left")==("Left"):
                                          motorControl.motorControl(3)
                                          print("Motor Left")
                            elif request.form.get("Right")==("Right"):
                                          motorControl.motorControl(4)
                                          print("Motor Right")
                            else:
                                          return render_template('index.html',pinouts=config.PINS.keys())

              elif request.method == 'GET':
                            print("No Post Back Call")
              return render_template('index.html',pinouts=config.PINS.keys())


@app.route('/update', methods=['POST'])
def update():
              return jsonify({
                            'title': 'Sensor Values',
                            'lineValue': lineValue,'distValue':distValue
                            })
if __name__ == '__main__':
              app.run(host='0.0.0.0')

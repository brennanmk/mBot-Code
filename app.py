from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import mBot.motorControl as motorControl
import mBot.lineSensor as lineSensor
import mBot.distanceSensor as distanceSensor
import mBot.bot_config as config
import threading
import time

# Setup flask app
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
running = True

# Setup bot components
line = lineSensor.LineSensor(config.PINS['line/sense'])
distance = distanceSensor.DistanceSensor(config.PINS['ultrasonic/trigger'],config.PINS['ultrasonic/echo'])

value = line.read()

def updateSensor():
              global value

              print('start of thread')
              while running: # global variable to stop loop
                            value = line.read()
                            time.sleep(1)
              print('stop of thread')
              
@app.route("/")
def indexRefresh(device=None, action=None):
              threading.Thread(target=updateSensor).start()
              return render_template('index.html')

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
                                          return render_template('index.html')

              elif request.method == 'GET':
                            print("No Post Back Call")
              return render_template('index.html')

@app.route("/editor",methods=['GET','POST'])
def editor():
    if request.method == 'GET':
        return render_template('editor.html')
    else:
        print(request.form.get("code"))


@app.route('/update', methods=['POST'])
def update():
              return jsonify({
                            'title': 'Line Finder',
                            'value': value
                            })
if __name__ == '__main__':
              app.run()
                  

from flask import Flask, render_template, request
from motor import Motor

app = Flask(__name__)

motorLeft = Motor(35,23,24)
motorRight = Motor(17,22,27)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('Forward') == 'Forward':
            motorRight.write(100)
            motorLeft.write(100)
            print("Motor Forward")

        elif request.form.get('Stop') == 'Stop':
            motorRight.write(0)
            motorLeft.write(0)
            print("Motor Stop")

        elif request.form.get('Backwards') == 'Backwards':
            motorRight.write(-100)
            motorLeft.write(-100)
            print("Motor Back")

        elif request.form.get("Left")==("Left"):
            motorRight.write(100)
            motorLeft.write(-100)
            print("Motor Left")

        elif request.form.get("Right")==("Right"):
            motorRight.write(-100)
            motorLeft.write(100)
            print("Motor Right")

        else:
            return render_template("index.html")
    elif request.method == 'GET':
            print("No Post Back Call")
    
    return render_template("index.html")         

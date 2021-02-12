from flask import Flask, render_template, request, jsonify
import os
import codecs
import subprocess
import robot.robot as bot
import robot.bot_config as config
import threading
import time

# Setup flask app and web socket
app = Flask(__name__)

# Are we currently executing code?
current_process = None
killed = False
running = True

bot.init()

# Setup bot components
lineValue = bot.getLineSensor()

distValue = bot.getDistanceCM()

# Thread used to update sensor values
def updateSensor():
    global lineValue, distValue, running
    print('start of thread')
    while running:  # global variable to stop loop
        lineValue = bot.getLineSensor()
        distValue = bot.getDistanceCM()
        time.sleep(1)
    print('stop of thread')

# Index
@app.route("/")
def indexRefresh(device=None, action=None):
    threading.Thread(target=updateSensor).start()
    return render_template('index.html')

# Used for motor control
@app.route("/", methods=['POST'])
def index():
    bot.cleanup()
    bot.init()
    if request.method == 'POST':

        power = int(request.form.get('Power'))
        power = min(100,max(power,1))
        print(power)

        if request.form.get('Forward') == 'Forward':
            bot.setMotorPower("LEFT", power)
            bot.setMotorPower("RIGHT", power)
            print("Motor Forward")
        elif request.form.get('Stop') == 'Stop':
            bot.setMotorPower("LEFT", 0)
            bot.setMotorPower("RIGHT", 0)
            print("Motor Stop")
        elif request.form.get('Backwards') == 'Backwards':
            bot.setMotorPower("LEFT", -power)
            bot.setMotorPower("RIGHT", -power)
            print("Motor Back")
        elif request.form.get("Left") == ("Left"):
            bot.setMotorPower("LEFT", -power)
            bot.setMotorPower("RIGHT", power)
            print("Motor Left")
        elif request.form.get("Right") == ("Right"):
            bot.setMotorPower("LEFT", power)
            bot.setMotorPower("RIGHT", -power)
            print("Motor Right")
    return render_template('index.html')


@app.route('/update', methods=['POST'])
def update():
    return jsonify({
        'title': 'Sensor Values',
        'lineValue': lineValue, 'distValue': distValue
    })

# Blockly editor HTML
@app.route("/blockly", methods=['GET'])
def blockly():
    return render_template('blockly.html')

@app.route("/docs",methods=['GET'])
def docs():
    return render_template('docs.html')

# Execute code
@app.route("/execute", methods=['POST'])
def execute():

    global current_process
    global killed
    global running

    action = request.form.get('action')
    if action == 'execute':
        # Run code
        if current_process != None:
            return 'BUSY'
        else:
            code = request.form.get('code')

            # Try and create file
            file_path = create_python_file(code)

            if file_path:
                run_python_file(file_path)
            else:
                return 'ERROR'

            if not killed:
                return 'DONE'
            else:
                killed = False
                return 'STOPPED'

    elif action == 'stop':
        # Stop code execution
        if current_process != None:
            killed = True
            running = False
            current_process.kill()
            return 'STOPPED'
        else:
            return 'IDLE'
    
    elif action == 'shutdown':
        # Shut down the pi
        bot.cleanup()

        # Kill current process if it's running
        if current_process != None:
            current_process.kill()
            killed = True

        subprocess.call("sudo shutdown -h now",shell=True)

        return 'SHUTDOWN'



# Create a python file to execute
def create_python_file(code):

    # Append bot code
    code = "import robot.robot as robot\nrobot.init()\nimport time\n" + \
        code + '\nrobot.cleanup()'

    file_path = os.path.join(os.getcwd(), 'temp.py')
    try:
        python_file = codecs.open(file_path, 'wb+', encoding='utf-8')
        try:
            python_file.write(code)
        finally:
            python_file.close()
    except Exception as e:
        print(e)
        print('Python file could not be created !!!')
        return None
    return file_path


# Run a created python file
def run_python_file(location):

    global current_process

    # Generate command
    cli_command = ['python3', location]
    print('CLI command: %s' % ' '.join(cli_command))

    # Run new process
    current_process = subprocess.Popen(
        cli_command, stdout=subprocess.PIPE, text=True)
    # Feed output to console
    output = current_process.communicate()
    current_process.wait()
    print(output[0])

    current_process = None


# Program entrypoint
if __name__ == '__main__':
    app.run(host='0.0.0.0')

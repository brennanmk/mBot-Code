from flask import Flask, render_template, request, jsonify
import os
import codecs
import subprocess

# Setup flask app and web socket
app = Flask(__name__)

# Are we currently executing code?
current_process = None
killed = False

# Default html
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Execute code
@app.route("/execute",methods=['POST'])
def execute():

    global current_process
    global killed

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
            current_process.kill()
            return 'STOPPED'
        else:
            return 'IDLE'

# Create a python file to execute
def create_python_file(code):

    # Append robot code
    code = "import robot.robot as robot\nrobot.init()\nimport time\n" + code + '\nrobot.cleanup()'

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
    current_process = subprocess.Popen(cli_command, stdout=subprocess.PIPE, text=True)
    # Feed output to console
    output = current_process.communicate()
    current_process.wait()
    print(output[0])

    current_process = None


# Program entrypoint
if __name__ == '__main__':
    app.run(host='0.0.0.0')

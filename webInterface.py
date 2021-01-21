from flask import Flask, render_template, request
import motorControl

app = Flask(__name__)

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
                                          return render_template("index.html")
              elif request.method == 'GET':
                            print("No Post Back Call")
              return render_template("index.html")
                                                      
if __name__ == '__main__':
              app.run()
                  

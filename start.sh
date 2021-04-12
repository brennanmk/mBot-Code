#!/bin/bash

# start.sh is used to start the app.py script on startup, this sh file is ran by a service at start in the provided ISO. 

screen -S app -dm bash -c "cd /home/pi/witBot-Code ; python3 app.py"

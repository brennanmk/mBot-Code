#!/bin/sh

#start blockly server, connect via http://ip:8080/Blockly
screen -dmS Blockly python3 Blockly/server.py

#start mBot control panel, connect via http://ip:5000
screen -dmS mBot python3 mBot/app.py

echo "mBot Started"

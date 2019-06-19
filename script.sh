#!/bin/bash
cd /home/pi/DOSIFICADOR
git pull origin master
python servo.py &

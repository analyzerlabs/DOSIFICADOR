#!/bin/bash
cd /home/pi/DOSIFICADOR
while true;do
	git pull origin master
	python servo.py &
	sleep 4
	echo "Nueva Dosificacion"
done

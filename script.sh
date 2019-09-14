#!/bin/bash
cd /home/pi/DOSIFICADOR

while true;do
	echo "====================================="
	echo "============ Actualizando ==========="
	sudo git pull origin master
	echo "====================================="
	echo "========== Ejecuta Software ========="
	sudo python limaem.py &
	sleep 14400
done

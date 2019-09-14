#!/bin/bash
cd /home/pi/DOSIFICADOR

while true;do
	echo "====================================="
	echo "============ Actualizando ==========="
	git pull origin master
	echo "====================================="
	echo "========== Ejecuta Software ========="
	python limaem.py &
	sleep 14400
done

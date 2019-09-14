#!/bin/bash
cd /home/pi/DOSIFICADOR

while true;do 
    echo "==============================="
    echo "========  ACTUALIZANDO  ======="
    echo "==============================="
    sudo git reset --hard
    sudo git pull
    echo "==============================="
    echo "========  EJECUTANDO..  ======="
    echo "==============================="
    sudo /home/pi/DOSIFICADOR/script.sh &
    sleep 14400
done
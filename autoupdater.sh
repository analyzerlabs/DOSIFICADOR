#!/bin/bash
cd /home/pi/DOSIFICADOR

while true;do 
    echo "==========================="
    echo "======  ACTUALIZANDO  ====="
    echo "==========================="

    sudo git clone git://github.com/analyzerlabs/DOSIFICADOR.git

    echo "==========================="
    echo "======  EJECUTANDO..  ====="
    echo "==========================="

    sudo /home/pi/DOSIFICADOR/script.sh &
    sleep 14400
done
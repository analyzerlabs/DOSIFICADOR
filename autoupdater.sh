#!/bin/bash
cd /home/pi/DOSIFICADOR
start=`date +%s`
while true;do
    end=`date +%s`
    runtime=$((end-start))
    echo $runtime
    if [ $runtime -gt 299 ]
        then
        start=`date +%s`
        runtime=$((end-start))
        echo "==============================="
        echo "========  ACTUALIZANDO  ======="
        echo "==============================="
        sudo cp /home/pi/DOSIFICADOR/revision.py /home/pi/revision
        sudo git reset --hard
        sudo git pull
        echo "==============================="
        echo "========  EJECUTANDO..  ======="
        echo "==============================="
        sudo /home/pi/DOSIFICADOR/script.sh &
    fi

done
#!/bin/bash
cd /home/pi/DOSIFICADOR
start=`date +%s`
while true;do
    end=`date +%s`
    runtime=$((end-start))
    hour=`date +%H`
    minute=`date +%M`
    echo $minute
    a=$(expr $hour % 4)
    b=$(expr $minute % 10)
    if [ $runtime -gt 60 ]
        then
        start=`date +%s`
        runtime=$((end-start))
        echo "==============================="
        echo "========  ACTUALIZANDO  ======="
        echo "==============================="
        sudo cp /home/pi/DOSIFICADOR/revision.py /home/pi/revision
        sudo git reset --hard
        sudo git pull
    fi
    
    if [ $b -eq 0 ]
        then
        echo "==============================="
        echo "========  ITS ALIVE ..  ======="
        echo "==============================="
        sudo python /home/pi/DOSIFICADOR/itsalive.py
    fi

    if [ $a -eq 3 ]
        then
                if [ $minute -eq 10 ]
                then
                echo "==============================="
                echo "========  EJECUTANDO..  ======="
                echo "==============================="
                sudo /home/pi/DOSIFICADOR/script.sh &
                sleep 60
                fi
    fi

done

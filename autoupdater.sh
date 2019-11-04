#!/bin/bash
cd /home/pi/DOSIFICADOR
start=`date +%s`
start2=`date +%s`
while true;do
    end=`date +%s`
    end2=`date +%s`
    runtime=$((end-start))
    runtime2=$((end-start))
    hour=`date +%H`
    minute=`date +%M`
    a=$(expr $hour % 4)
    b=$(expr $minute % 10)
    if [ $runtime -gt 60 ]
        then
        echo $hour:$minute
        start=`date +%s`
        runtime=$((end-start))
        echo "==============================="
        echo "========  ACTUALIZANDO  ======="
        echo "==============================="
        sudo git reset --hard
        sudo git pull
        sudo python /home/pi/DOSIFICADOR/myemail.py &
    fi
    
    if [ $runtime2 -gt 300 ]
        then
        start2=`date +%s`
        echo "==============================="
        echo "========  ITS ALIVE ..  ======="
        echo "==============================="
        sudo python /home/pi/DOSIFICADOR/itsalive.py &
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

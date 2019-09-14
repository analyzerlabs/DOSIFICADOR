#!/bin/bash
cd C:/Users/Milkito/Documents/Github/DOSIFICADOR

echo "please enter your name:"
read myname
echo "ypu entered: $myname"

myvar=1

while [ $myvar -le 10 ]
do
	echo $myvar
	myvar=$(($myvar + 1))	
	sleep 1
done

if [ -f ~/limaem.py]
then
	echo "the file exist"
else 
	echo "file doesnt exist!!"
fi

while true;do
	echo "pid is $$"
	echo $$ > /tmp/$(basename $0).pid
    echo "====================================="
	echo "============ Actualizando ==========="
	git pull origin master
	echo "====================================="
	echo "========== Ejecuta Software ========="
	python limaem.py &
	sleep 400
done

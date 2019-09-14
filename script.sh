#!/bin/bash
cd /home/pi/DOSIFICADOR

sudo git pull origin master
echo "===== ejecutando python file ====="
sudo python limaem.py &

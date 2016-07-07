#!/bin/bash

#Auto run this project when raspi power on.

script_path=$(pwd)/ip_speaker.py

echo 'This script`s path is ok?'
echo $script_path
echo 'Check it and maybe you should edit it in /etc/rc.local'

#Add auto run script to rc.local
sudo sed -i "/^exit 0/i python $script_path &" /etc/rc.local

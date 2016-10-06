#!/bin/bash

# auto run this project when raspi power on.

script_path=$(pwd)/ip_speaker.py

echo 'This script`s path is ok?'
echo $script_path
echo 'Check it and maybe you should edit it in /lib/systemd/system/ip_speaker.service'

# make systemd service
sed "/^\[Install\]/i ExecStart=$script_path \n" ./tools/ip_speaker.service.template > ./tools/ip_speaker.service

# copy to '/lib/systemd/system'
sudo cp ./tools/ip_speaker.service /lib/systemd/system

# enable auto start
sudo systemctl enable ip_speaker

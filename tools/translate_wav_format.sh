#!/bin/bash

#Translate wav format that can be play by aplay.

for file in ./*wav
do
  echo $file
  ffmpeg -i -y $file $file
done

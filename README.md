# Ip speaker

Ip speaker for raspberry pi.
Inspired by this [project](https://github.com/ma6174/speak_raspi_ip), use aplay(build in) to paly wav files, and more feature.

## Feature

* Can help you get the ip address of your raspberry pi when the raspi power on.
* Auto close up when you ssh in your raspi or the raspi has turned up more than 10 mins.

## How to use

* Git clone or downlode in somewhere.
* Run tools/setup.sh(be careful about script path).
* Plug in headphones when the raspi power on, and listen it`s ip address.

## About wav file source

I download on this [site](https://evolution.voxeo.com/library/audio/prompts/numbers/index.jsp)

Make sure the wav file can be played by aplay, I use ffmpeg to translate format, like this:

```shell
ffmpeg -i 0.wav 0.wav
```

The wav files in this project have been converted.

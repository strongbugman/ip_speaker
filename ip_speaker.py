#!/usr/bin/env python
"""
Speak ip address by aplay.
"""

import os
import time

def speakip(ip, sleeptime=1):
    '''
    Intro: use 'aplay' to speak ip
    Parameter:
        ip: str - ip like '192.168.1.1'
        sleep_time - sleep time when speak '.'
    Return: no return
    '''
    #paly [num].wav by aplay
    playip_cmd = "aplay data/{:s}.wav"
    for char in ip:
        if char != '.':
            os.system(playip_cmd.format(char))
        else:
            time.sleep(sleeptime)

def getips():
    '''
    Intro: use shell cmd to get ip address, no '127.*'
    Return:
        ips: list - ip list
    '''
    #Get ips by extracting the out of ifconfig cmd
    getips_cmd = "ifconfig | grep Mask | awk ' {print $2}' | cut -d: -f2 | grep -v '^127'"
    ips = os.popen(getips_cmd).read()
    return ips.split('\n')[:-1]

def isssh():
    '''
    Intro: juge if someone ssh in
    Return:
        True or False
    '''
    #if someone ssh in, the pid of sshd will more than 2
    is_ssh_cmd = "pidof sshd | cut -d ' ' -f2"
    sshpid = os.popen(is_ssh_cmd).read()
    return len(sshpid) > 1

def outoftime(starttime, maxtime=600):
    '''
    Intro: juge if this run time out of max time, default 10 mins
    Return:
        True or False
    '''
    return (time.time() - starttime) > maxtime

def main(sleeptime=5):
    starttime = time.time()

    while True:
        if isssh() or outoftime(starttime):
            break
        for ip in getips():
            speakip(ip)
            time.sleep(sleeptime)

if __name__ == '__main__':
    main()

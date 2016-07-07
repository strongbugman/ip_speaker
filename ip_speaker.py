#!/usr/bin/env python
"""
Speak ip address by aplay.
"""

import os
import sys
import time

def sleep(sleeptime):
    '''
    Intro: print sleep time and sleep.
    parameter:
        sleeptime: int - sleep time, s
    '''
    print 'sleep:', sleeptime, 's'
    time.sleep(sleeptime)

def speakip(ip, sleeptime=1):
    '''
    Intro: use 'aplay' to speak ip
    Parameter:
        ip: str - ip like '192.168.1.1'
        sleep_time - sleep time when speak '.'
    Return: no return
    '''
    #paly [num].wav by aplay
    playip_cmd = "aplay {:s}/data/{:s}.wav"
    for char in ip:
        if char != '.':
            os.system(playip_cmd.format(sys.path[0], char))
        else:
            sleep(sleeptime)

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

def sshin():
    '''
    Intro: juge if someone ssh in
    Return:
        True or False
    '''
    #if someone ssh in, the pid of sshd will more than 2
    is_ssh_cmd = "pidof sshd | awk '{print NF}'"
    sshpid = os.popen(is_ssh_cmd).read()
    return int(sshpid) > 1

def outoftime(starttime, maxtime=600):
    '''
    Intro: juge if this run time out of max time, default 10 mins
    Return:
        True or False
    '''
    return (time.time() - starttime) > maxtime

def test(sleeptime):
    '''
    Test.
    '''
    for ip in getips():
        speakip(ip)
        sleep(sleeptime)
    

def main(sleeptime=5):
    starttime = time.time()
   
    if 'test' in sys.argv:
        test(sleeptime)
        sys.exit()

    while True:
        if sshin() or outoftime(starttime):
            break
        for ip in getips():
            speakip(ip)
            sleep(sleeptime)

if __name__ == '__main__':
    main()

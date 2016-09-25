#!/usr/bin/env python2
"""
Speak ip address by aplay.
"""

import os
import sys
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
    playip_cmd = "aplay {:s}/data/{:s}.wav"
    for char in ip:
        if char != '.':
            os.system(playip_cmd.format(sys.path[0], char))
        else:
            time.sleep(sleeptime)

def getips():
    '''
    Intro: use shell cmd to get ip address, no '127.*'
    Return:
        ips: list - ip list
    '''
    #Get ips by extracting the out of ifconfig cmd
    getips_cmd = "ifconfig | grep inet | grep -v \"inet6\" | awk ' {print $2}' | cut -d: -f2 | grep -v '^127'"
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
    try:
        return int(sshpid) > 1
    except ValueError:
        return False


def main(sleeptime=5, count=200):
    '''
    sleeptime - sleeptime for time interval bettwen two complete ip`s speaking
    count - how much times for ip speaking
    '''
    if 'test' in sys.argv:
        for ip in getips():
            speakip(ip)
            print 'sleep:', sleeptime, 's'
            time.sleep(sleeptime)

    while count > 0:
        if sshin():
            break
        for ip in getips():
            speakip(ip)
            time.sleep(sleeptime)
        count -= 1

if __name__ == '__main__':
    main()

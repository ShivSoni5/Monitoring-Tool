#!/usr/bin/env pyhton

#CLIENT

import socket,commands as cmd


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host="192.168.10.239"
port=9999

lis=[]

# MODEL
a="lscpu | grep -i 'model name'|awk -F : '{print $2}'"

# Architecture
b="lscpu | grep -i 'architecture' | awk -F : '{print $2}'"

# OS
c="cat /etc/redhat-release"

# HDD
d="lsblk | awk '{print $4}' | head -2 | tail -1"

# RAM (in MB)
e="free -lm | awk '{print $2}'| head -2|tail -1"

# Battery status
#f="upower -i /org/freedesktop/UPower/devices/battery_BAT0|grep -E 'state|to\ full|percentage'"

# Virtualization support
g="lscpu | grep -i 'virtualization' | awk -F : '{print $2}'"

# CPU op-mode(s)
h="lscpu | grep -i 'CPU op-mode' | awk -F : '{print $2}'"

clis=[a, b, c, d, e, g, h]

def making_list(lis,cmdlis):
	for i in cmdlis:
		c=cmd.getoutput(i)
		lis.append(c.strip())

making_list(lis,clis)

for  i in lis:
	s.sendto(i,(host,port))




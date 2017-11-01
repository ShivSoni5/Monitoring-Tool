#!/usr/bin/env python

#SERVER


import sys,socket
import os,commands as cmd
"""
ips=sys.argv[1]

s=cmd.getoutput("nmap -F '"+ips+"' | grep -i  '^nmap scan ' | awk -F ' ' '{print $6}'")

conn = s.strip("()").split(")\n(")
print conn
"""
def create_data_file():
	if not os.path.exists("/root/Desktop/data.txt"):
		f=open("/root/Desktop/data.txt",'w')
		f.write("IP       :     MODEL                              : ARCH :              OPERATING SYSTEM                     : HDD  :RAM :VIRT: CPU op-mode(s)\n\n")
		f.close()

create_data_file()


#def send_client_file():

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host="192.168.10.239"
port=9999
s.bind((host,port))

for i in range(7):
	data=s.recvfrom(1024)
	f=open("/root/Desktop/data.txt","a")
	if i == 0:
		f.write(data[1][0]+":"+data[0]+":")
	elif i == 6:
		f.write(data[0]+"\n\n")
	else:
		f.write(data[0]+":")	
	f.close()

from pwn import *
import sys
import time
import re
import math

result = "nothing"
conn = remote("irc.root-me.org",6667) 
print conn.recvline()

channel="#root-me_challenge\r\n"

conn.send("USER wizardleet wizardleet wizardleet :wizardleet\r\n")
conn.send("NICK wizardleet\r\n")

print conn.recv()


conn.send("JOIN "+channel)
 
time.sleep(1)
 
conn.send("PRIVMSG candy !ep2\r\n") 

servmsg = conn.recv()

print servmsg

time.sleep(1)
botresp = conn.recv() 
listing = botresp.split()

print "\n "+listing[-1]
buf = listing[-1]
result = buf.replace(':','')


print "decoding ..\n"
decoded = result.decode('base64','strict')

conn.send("PRIVMSG candy !ep2 -rep "+decoded+"\r\n")
print "sending..\r\n"

print conn.recv()

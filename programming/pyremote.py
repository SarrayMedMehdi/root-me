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

buff = "!ep1\r\n" 
bot = "candy\r"

conn.send("JOIN "+channel)

#joined = conn.recv() 
 
time.sleep(2)
 
conn.send("PRIVMSG candy !ep1\r\n") 

#time.sleep(2)
#print "msg sent"
servmsg = conn.recv()

print servmsg

time.sleep(1)
botresp = conn.recv() 

result = re.search(r'\d*\s[/]\s\d*',botresp)
print "\n got the string: "+result.group()
laststring = result.group().split('/') 
total = math.sqrt(int(''.join(laststring[0].strip()))) * int(''.join(laststring[1].strip())) 

total = round(total,2)


print "\n THIS is the number="
print total
print "\n"

T = str(total)

conn.send("PRIVMSG candy !ep1 -rep "+T+"\r\n")
print "sending..\r\n"

print conn.recv()

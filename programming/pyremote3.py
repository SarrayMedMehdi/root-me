from pwn import *
import sys
import time
import codecs

result = "nothing"
conn = remote("irc.root-me.org",6667) 
print conn.recvline()

channel="#root-me_challenge\r\n"

conn.send("USER wizardleet wizardleet wizardleet :wizardleet\r\n")
conn.send("NICK wizardleet\r\n")

print conn.recv()


conn.send("JOIN "+channel)
 
time.sleep(1)
 
conn.send("PRIVMSG candy !ep3\r\n") 

servmsg = conn.recv()

print servmsg

time.sleep(1)
botresp = ''
botresp = conn.recv() 

if  botresp:
    listing = botresp.split()
    print "\n "+listing[-1]
    buf = listing[-1]
    result = buf.replace(':','')
    result = codecs.decode(result,'rot_13')
    print "decoding ..\n"+result


conn.send("PRIVMSG candy !ep3 -rep "+result+"\r\n")
print "sending..\r\n"

print conn.recv()

from pwn import *
import sys
import time
import codecs
import zlib
import base64
import sys
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
sys.stdout.flush()
print botresp

if  botresp:
    listing = botresp.split()
    print "\n "+listing[-1]
    buf = listing[-1]
    result = buf.replace(':','')
    print "\n"+result
    result = result.decode('base64').decode('zlib')
    #result = base64.b64decode(result)
   # print "base64 decoding ..\n"+result
    #result = zlib.decompress(result)
    print "\n base64 decoding and zlib decompressing.. "+result
    
conn.send("PRIVMSG candy !ep3 -rep "+result+"\r\n")
print "sending..\r\n"

print conn.recv()


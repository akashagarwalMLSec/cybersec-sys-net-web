#!/usr/bin/env python3
from scapy.all import *
a = IP()
a.dst = '8.8.8.8'
a.ttl = 14
b = ICMP()
send(a/b)

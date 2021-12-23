#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-dcfe338ef981,enp0s3',filter='icmp',prn=print_pkt )


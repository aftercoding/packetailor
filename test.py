
import sys
from scapy.all import sr1,IP,ICMP


ip = "IP"
p=sr1(eval(ip)(dst="192.168.0.1")/ICMP())
if p:
    p.show()

print("hello world")

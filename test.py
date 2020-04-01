
import sys
from scapy.all import sr1,IP,ICMP


ip = "IP"
str1 = 'IP(dst="192.168.0.1")/ICMP()'

#p=sr1(eval(ip)(dst="192.168.0.1")/ICMP())
p = sr1(eval(str1))
if p:
    p.show()

print("hello world")


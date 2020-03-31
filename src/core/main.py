#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP

class LayerData(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(ClassName, self).__init__()
		self.name = None
		self.attribute = None
	


protocol1 = "IP"
ipdst = "192.168.0.1"
protocol2 = "ICMP"

p=sr1(eval(protocol1)(dst= ipdst)/eval(protocol2)())
if p:
    p.show()
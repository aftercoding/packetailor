#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP

class LayerData(object):
	"""docstring for ClassName"""
	def __init__(self,name):
		#super(ClassName, self).__init__()
		self.name = name
		self.attribute = None
	
	def setAttribute(self):
		self.attribute = {'dst': '192.168.0.1'}


layerData1 = LayerData('IP')
layerData1.setAttribute()
layerData2 = LayerData('ICMP')

cmdStr = layerData1.name + '(' + 'dst' + '=' + ' \'192.168.0.1\'' + ')' +'/' + layerData2.name +'(' +''+ ')'

print (cmdStr)


p = sr1(eval(cmdStr))
if p:
	p.show()

#p=sr1(eval(protocol1)(dst= ipdst)/eval(protocol2)())
#if p:
#    p.show()
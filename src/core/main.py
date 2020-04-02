#! /usr/bin/env python

import sys
from packetSuiter import *

#cmdStr = layerData1.name + '(' + 'dst' + '=' + ' \'192.168.0.1\'' + ')' +'/' + layerData2.name +'(' +''+ ')'

#print (cmdStr)

p = PacketSuiter()

p.loadSuite()
p.run()


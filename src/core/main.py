#! /usr/bin/env python

import sys
from packetSuiter import *

p = PacketSuiter()

p.loadSuite('D:\\packetailor\\samples\\ip-icmp.json')
p.run()


#! /usr/bin/env python

import sys
from packetSuiter import *

p = PacketSuiter()

p.loadSuite('D:\\packetailor\\samples\\dns.json')
p.run()


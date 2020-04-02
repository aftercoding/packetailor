
from scapy.all import sr1,IP,ICMP,Send

class PacketSuiter(object):
	"""docstring for PacketSuiter"""
	def __init__(self, arg):
		super(PacketSuiter, self).__init__()
		self.arg = arg
	
	def loadSuite(packetSuite):
		pass
	def executeCmd(actionType,cmdStr):
		if (actionType is 'Send'):
			p = Send(eval(cmdStr))
		elif(actionType is 'Sr'):
			p = sr1(eval(cmdStr))
		else:
			print('Wrong action Type')

	def run():
		pass

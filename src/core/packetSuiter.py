
from scapy.all import *
from suiteParser import *
class PacketSuiter(object):
	"""docstring for PacketSuiter"""
	def __init__(self):
		super(PacketSuiter, self).__init__()
		self.actionType = 'Sr'
		self.layerDataList = None
		# self.cmdStr = ""
	
	def loadSuite(self,packetSuite):
		pass
	def jointCmd(self):
		ld1 = LayerData("IP")
		ld1.setAttribute({'dst': '192.168.0.1'})
		ld2 = LayerData("ICMP")
		layerDataList = [ld1,ld2]
		cmdStr = ""
		for ld in layerDataList :
			cmdStr += ld.name +'('
			attributeDict = ld.getAttribute()
			if(attributeDict is not None):
				for key in attributeDict :
					print (key)
					cmdStr += key
					cmdStr += '=\''
					cmdStr += attributeDict[key]
					cmdStr += '\'' + ')'
				cmdStr +='/'
		cmdStr +=')'
		print (cmdStr)

		return cmdStr


	def executeCmd(self):
		if (self.actionType is 'Send'):
			p = Send(eval(self.jointCmd()))
		elif(self.actionType is 'Sr'):
			p = sr1(eval(self.jointCmd()))
		else:
			print('Wrong action Type')

	def run(self):
		self.executeCmd()

if __name__ == '__main__':   
	p = PacketSuiter()
	p.jointCmd()

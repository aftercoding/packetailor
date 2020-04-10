
from scapy.all import *
from suiteParser import *
class PacketSuiter(object):
	"""docstring for PacketSuiter"""
	def __init__(self):
		super(PacketSuiter, self).__init__()
		self.actionType = 'Sr'
		self.layerDataList = []
	
	def setActionType(self, actionType):
		self.actionType = actionType

	def loadSuite(self,packetSuite):
		with open(packetSuite,'r') as f:
			data = json.load(f)
		# print(data)
		for key in data:
			ld = LayerData(key)
			ld.setAttribute(data[key])
			self.layerDataList.append(ld)

	def jointCmd(self):
		cmdStr = ""
		for ld in self.layerDataList:
			cmdStr += ld.name +'('
			attributeDict = ld.getAttribute()
			if(attributeDict):
				for key in attributeDict :
					cmdStr += key
					cmdStr += '='					
					if(isinstance(attributeDict[key],int)):
						cmdStr += str(attributeDict[key])
					else:
						cmdStr += '\''
						cmdStr += attributeDict[key]
						cmdStr +='\''
					cmdStr += ','
				cmdStr = cmdStr[:-1]
			cmdStr += ')'
			cmdStr +='/'
		cmdStr = cmdStr[:-1]
		print (cmdStr)
		return cmdStr

	def executeCmd(self):
		if (self.actionType is 'send'):
			p = send(eval(self.jointCmd()))
		elif(self.actionType is 'Sr'):
			p = sr1(eval(self.jointCmd()))
		else:
			print('Wrong action Type')

	def run(self):
		self.executeCmd()

if __name__ == '__main__':   
	p = PacketSuiter()
	p.setActionType('send')
	p.loadSuite('D:\\packetailor\\samples\\ip-tcp.json')
	# p.loadSuite('D:\\packetailor\\samples\\ip-icmp.json')
	# p.jointCmd()
	p.executeCmd()

	# sr1(eval("IP(dst=\"192.168.0.1\")/UDP()/DNS(rd=1,qd=DNSQR(qname=\"www.slashdot.org\"))"))
class SuiteParser(object):
	"""docstring for SuiteP
arser"""
	def __init__(self, arg):
		super(SuiteParser, self).__init__()
		self.arg = arg
		


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
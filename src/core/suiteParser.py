# import sys

		

class LayerData(object):
	"""docstring for ClassName"""
	def __init__(self,name):
		#super(ClassName, self).__init__()
		self.name = name
		self.attribute = None
	
	def setAttribute(self,attribute):
		# self.attribute = {'dst': '192.168.0.1'}
		self.attribute = attribute

	def getAttribute(self):
		return self.attribute 

# layerData1 = LayerData('IP')
# layerData1.setAttribute()
# layerData2 = LayerData('ICMP')
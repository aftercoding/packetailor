import sys
import os.path

import json 
		

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


# data = {
#     'protocol-name' : 'IP',
#    'dst': '192.168.0.3',
# }

# with open('data.json', 'w') as f:
#     json.dump(data, f)

with open('D:\\packetailor\\samples\\ip-icmp.json', 'r') as f:
# with open('data.json', 'r') as f:
    data = json.load(f)
print (data)

# with open ('D:\\packetailor\\samples\\ip-icmp.json',"r") as f:
# 	temp = json.loads(f.read())
# 	print(temp)



# f = open('D:\\packetailor\\samples\\ip-icmp.json',"r")
# # print(f.readlines())

# print (js.load(f))
# f.close()
# layerData1 = LayerData('IP')
# layerData1.setAttribute()
# layerData2 = LayerData('ICMP')
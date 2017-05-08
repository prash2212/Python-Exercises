import sys

class BoundUnbound:
	def __init__(self):
		pass
	def funcWithObj(self,name):
		print (name)
	def funcWithoutObj(name):
		print (name)
		
obj = BoundUnbound()
#BoundUnbound.funcWithObj(obj,'prash')
funccall = BoundUnbound.funcWithObj
funccall(obj,'prash')


BoundUnbound.funcWithoutObj('prash without object')
print (obj.__class__.__name__)
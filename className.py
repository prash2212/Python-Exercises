import sys

class Emp:
	def __init__(self,name):
		self.firstname = name
	__X = 10
	def qualification(self):
		print (__X)
		
obj = Emp('prash')
print (Emp.__name__)
print (Emp.__dict__)
#obj = Emp()
print (obj._Emp__X)
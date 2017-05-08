import sys

class prop:
	def setage(self,age):
		self.__dict__['age'] = age
		
	def getage(self):
		return self.__dict__['age']
		
	age = property(getage,setage,None,None)
	
if __name__ == '__main__':
	obj = prop()
	obj2 = prop()
	obj.age = 4
	obj2.age = 20
	print (obj.age)
	print (obj2.age)

import sys

###Modify the same class that you get
'''
def classdeco(cls):
	cls.godfather = 'God Father'
	print('Just assigned god father')
	return cls
'''

###Or create a new class and ship it
def classdeco(cls):
	class deco():
		def __init__(self,*args):
			self.wrapped = cls(*args)
			self.godfather = 'God Father'
			print('Just assigned god father')
	return deco


@classdeco
class ClassA():
	def __init__(self,name):
		print("Inside ClassA Init function")
		self.name = name


if __name__ == '__main__' :
	print("In main function")
	obj = ClassA('prash')
	print('In main function, the attribute name is ' + obj.name)
	print('In main function, the attribute name is ' + obj.godfather)

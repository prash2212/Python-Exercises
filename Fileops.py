import sys

class Fileclass:
	def __init__(self,name):
		self.ff = open(name)
	def display(self):
		for i in self.ff:
			print(i)

objFile = Fileclass("classdeco.py")
objFile.display()
		

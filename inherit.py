import sys

class Parent:
	def __init__ (self):
		print ("parent class")
		self.name = "mommy"
	def __getattr__(self,attr):
		print("Hahaha Trapped you: " + attr)
	
class Child1(Parent):
	def __init__(self): 
		print ("child1 class")
		self.name = "Aryan"
	def __getattr__(self,attr):
		print("Am i __getattr__")
		if attr == 'name':
			print("Why do you want to know my name")
		else:
			print("Hahaha Trapped you: " + attr)
	
		
if __name__ == "__main__":
	oChild1 = Child1()
	print(oChild1.name)
	whois = getattr(oChild1,'name')
	print(whois)

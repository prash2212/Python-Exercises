import sys

class Commuter:
	def __init__(self,value):
		self.val = value
	def __add__(self,other):
		print ('add = ')
		if ( isinstance(other,Commuter)):
			return Commuter (other.val + self.val)
	def __radd__(self,other):
		print ('radd = ')
		#return other + self.val #didn't make a difference when changed the order for printing
		return self.val + other


x = Commuter(10)
y = Commuter(20)

'''
print (' x + y = ', x+9)
print (' x + y = ', 7 + y)
print (' x + y = ', x + y)
'''

z = x + y + 10
print (' z = ', z.val)
import sys

def deco(func):
	print('in the decorator')
	return func(10)

@deco
def function(value):
	print ('function print ' + str(value))
	

#function(22)
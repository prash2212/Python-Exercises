import sys

class classdeco:
	def __init__(self,funct):
		print("Classdeco Init function where the function called was " + funct.__name__)
		self.func = funct
	def __call__(self,*args):
		return self.func(args)


@classdeco
def function(num):
	print('Inside Function ' + str(num))
	return num

if __name__ == '__main__':
	print('Inside main')
	c=function(10)
	print ("Inside main, value of C is" + str(c[0]))

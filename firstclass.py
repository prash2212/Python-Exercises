import sys

class firstclass:
	def __init__(self,sent):
		self.sent = sent
		print ('I am in the firstclass constructor\n')
	def func(self):
		assert False, 'Have to implement this function'
		#print (self.sent,end='haha\n')

class secondclass(firstclass):
	
	def __init__(self,sent):
		self.sent = sent
		
	'''
	def func(self):
		#firstclass.func(self)
		print (self.sent + ' And now we are having twins\n')
	'''	
	
sent = 'my name is prashanth. My family is beautiful'
obj = secondclass(sent)
obj.func()

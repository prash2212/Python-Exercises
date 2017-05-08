import sys

class Iters:
	#a=10
	def __init__(self,value):
		self.data = value
		
	def __next__(self):
		print ('I am in next')
		for x in self.data:
			yield x
			
	def __getitem__(self,i):
		print ('I am in getitem')
		return self.data[i]
		
	def __getattr__(self,atr):
		print ('Get attribute method')
		if atr != 'a':
			print ('Atr is not equal to a')
			return self.__dict__[atr]
		else:
			raise AttributeError

if __name__ == '__main__':
	I = Iters([1,2,3,4,5])
	print (I[0])
	print (I.a)
	i = iter(I)
	next(i)
	next(i)
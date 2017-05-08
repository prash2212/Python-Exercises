import sys
from tkinter import *

class Callback:
	def __init__(self,color):
		self.color = color
	def __call__(self):
		print ('true ', self.color)
		
c1 = Callback('red')

Button(command=c1.color)
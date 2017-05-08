import sys
###from xml.etree.ElementTree import parse, dump
import xml.etree.ElementTree

ET = xml.etree.ElementTree

'''
filecontent = open(r'../../xmls/first.xml','r').read()
print(filecontent)
'''

tree = ET.parse(r'../../xmls/first.xml')
ET.dump(tree)
	
for E in tree.findall('Babies'):
	print (E.text)
	if isinstance(E,ET.Element):
		print ('Item is an element')


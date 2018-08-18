import requests
import json
import sys
from bs4 import BeautifulSoup

class News:
	url = ""
	def __init__(self):
		pass

	def getsite(self):
		pass;
		

class Match:
	def __init__(self,fname):
		self.fname = fname

	def getxml(self):
		with open(self.fname,"r") as html:
		 soup = BeautifulSoup(html,'lxml')
		return soup
		return soup.prettify() #It will display what tags are nested with each other

	def match(self):
		xml = self.getxml();
		info = []
		match = xml.find_all('batting')
		print(match)
		for m in match:
			print(m)
			print(m.runs.text)

def main():
	m = Match('cricket.xml')
	#print(m.getxml())
	m.match()

if __name__ == '__main__':
	main()


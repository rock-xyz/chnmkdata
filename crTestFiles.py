import os
import random


def numberoffiles():
	pass

def loopfiles():
	pass

def copyfile(orgfile,newfilename):
	fo = open(newfilename,"w")
	for line in open(orgfile):
		a=list(line.split("|"))
		if a[0] == "MD002":
			#random assign 
			tradeprice=float(a[9])
			tradeprice=random.random()*tradeprice
			a[9]=str(tradeprice)
			i=1
			newline = a[0]
			for i in range(1,33):
				newline=newline +"|"+a[i]
				#print(newline)
				i=i+1,
			fo.write(newline+"\n")
	fo.close()



if __name__ == '__main__':
	orgfile = "E:\\rock\\workspace\\mk\\mktdt00.txt"
	newfilename = "E:\\rock\\workspace\\mk\\mktdt01.txt"
	copyfile(orgfile,newfilename)

import os
import time,datetime
import re
#

def init(filename,filepath): #初始化股票列表
	#check if the file is updated, if not wait for 5s;

	#file is not existing

	i=0
	for i in range(1,100):
		if os.path.exists(filepath):
			stat_info=os.stat(filepath)
			modifyTime=time.ctime(stat_info.st_mtime)
			if h.get(filename) == None:
				h[filename]=modifyTime
				readfiles(filepath)
			else:
				if h.get(filename) == modifyTime:
					time.sleep(5)
					print(filename + ":" + str(modifyTime) + " -- Same")
				else:
					h[filename] = modifyTime
					print(filename + ":" + str(modifyTime) + " -- Diff")
					readfiles(filepath)
		else:
			print("File is not existing")
			time.sleep(10)

def loopfiles(sourceDir):
	for files in os.listdir(sourceDir):
		filepath = os.path.join(sourceDir,files)
		if re.match("mktdt0",files):
			print(filepath)
			readfiles(filepath)

def readfiles(filepath):
	linenum = 0
	chgnum = 0
	for line in open(filepath):
		a=list(line.split('|'))
		linenum = linenum + 1
		if a[0] == "MD002":
			securityid = a[1]
			#print("证券代码",securityid)
			securityname = a[2]
			#print("证券简称",securityname)
			tradevolume = a[3]
			#print("成交量",tradevolume)
			tradeprice=float(a[9])
			#print("最新价",tradeprice)
			tradetime = a[32]
			#print("报价时间",tradetime)  #需要把list结果编辑成消息

			checkhighprice(securityid,tradeprice)

			checklowprice(securityid,tradeprice)

			calchange(securityid)
	chgnum = g.get("chgnum")
	print("Total number of lines in file: " + str(linenum))
	print("Total price variance in files: " + str(chgnum))


def checkhighprice(securityid,tradeprice):
	if e.get(securityid) == None:
		e[securityid]=tradeprice
	else:
		if e.get(securityid)<tradeprice:
			e[securityid]=tradeprice		

def checklowprice(securityid,tradeprice):
	if f.get(securityid) == None:
		f[securityid]=tradeprice
	else:
		if f.get(securityid)>tradeprice:
			f[securityid]=tradeprice

def calchange(securityid):
	highprice = e.get(securityid)
	lowprice = f.get(securityid)

	if lowprice != 0:
		mv = abs(highprice - lowprice) / lowprice
		if mv > 0.1:
			chg = g.get("chgnum")
			g["chgnum"] = int(chg + 1)
			print(securityid+":",mv)

def currenttime():
	nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print(nowTime)	

if __name__ =="__main__":
	e={} #存储highprice
	f={} #存储lowprice
	g={} #number of price change
	h={} #time of file modified

	g["chgnum"] = 0
	currenttime()
	sourceDir = "E:\\rock\\workspace\\mk"
	#filename()
	filename = "mktdt00.txt"
	filepath = os.path.join(sourceDir,filename)
	
	init(filename,filepath)

	#loopfiles(sourceDir)

	#readfiles(filepath)

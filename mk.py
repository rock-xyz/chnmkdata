import os
import datetime
#

def init(): #初始化股票列表
	pass

def filename():
	if filename == None:
		filename = "mktdt00.txt"
	else:
		filename = "mktdt"+seq+".txt"


def readfiles(filepath):
	for line in open(filepath):
		a=list(line.split('|'))
		if a[0] == "MD002":
			securityid = a[1]
			print("证券代码",securityid)
			securityname = a[2]
			print("证券简称",securityname)
			tradevolume = a[3]
			print("成交量",tradevolume)
			tradeprice=float(a[9])
			print("最新价",tradeprice)
			tradetime = a[32]
			print("报价时间",tradetime)  #需要把list结果编辑成消息

			checkhighprice(securityid,tradeprice)

			checklowprice(securityid,tradeprice)

			calchange(securityid)


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
		print(mv)

def currenttime():
	nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print(nowTime)	

if __name__ =="__main__":
	e={} #存储highprice
	f={} #存储lowprice
	g={} #latest price
	
	currenttime()
	sourceDir = "e:\\mktest"
	#filename()
	filename = "mktdt00.txt"
	filepath = sourceDir+"\\"+filename
	print(filepath)

	readfiles(filepath)

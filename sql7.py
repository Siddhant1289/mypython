# to select data
import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
cur=db.cursor()
e=int(input('enter empno:'))
s="select * from employee where empno=%d"%(e)
try:
	cur.execute(s)
	res=cur.fetchall()
	for r in res:
		print("empno",r[0])
		print("name",r[1])
		print("city",r[2])
		print("salary",r[3])
except:
	print("any issue")
db.close()
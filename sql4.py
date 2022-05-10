import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
cur=db.cursor()
e=int(input('enter empno'))
n=input('enter name')
c=input('enter city')
sl=int(input('enter salary'))
s="insert into employee values(%d,'%s','%s',%d)"%(e,n,c,sl)
try:
	cur.execute(s)
	db.commit()
	print('record saved')
except Exception as es:
	print('any issue',es)
db.close()
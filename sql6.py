import pymysql         # to change data
db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
cur=db.cursor()
e=int(input('enter empno'))
n=input('enter name')
c=input('enter city')
sl=int(input('enter salary'))
s="update employee set name='%s',city='%s',salary=%d where empno=%d"%(n,c,sl,e)
try:
	cur.execute(s)
	db.commit()
	print('record changed')
except Exception as es:
	print('any issue',es)
db.close()
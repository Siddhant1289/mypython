import pymysql           # to dalete data
db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
cur=db.cursor()
e=int(input('enter empno'))
s="delete from employee where empno=%d"%(e)
try:
	cur.execute(s)
	db.commit()
	print('record deleted')
except Exception as es:
	print('any issue',es)
db.close()
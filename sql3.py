#TO ADD RECORD
import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
cur=db.cursor()
s="insert into employee values(107,'ANKIT','MATHURA',300400)"
try:
	cur.execute(s)
	db.commit()
	print('RECORD SAVED')
except:
	print("ANY ISSUE")
db.close()
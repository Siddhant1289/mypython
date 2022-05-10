# to display all data 
import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
cur=db.cursor()
s="select * from employee"
try:
	cur.execute(s)
	res=cur.fetchall()
	for r in res:
		print("empno",r[0],"name",r[1],"city",r[2],"salary",r[3])
		print("")
except:
	print("any issue")
db.close()
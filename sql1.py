import pymysql
db=pymysql.connect(host="localhost",user="root",password="root",database="factory")
cur=db.cursor()
cur.execute("select version()")
data=cur.fetchone()
print('DATABASE VERSSION IS',data)
db.close()
import mysqldb as sql
host="localhost"
user="appu.s"
password="root"
db='python_db'
conn=sql.connect(host=hosst,user=user,password=password,db=db)
cur=conn.cursor()
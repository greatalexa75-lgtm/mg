import mysqldb as sql
host="localhost"
user="mg"
password="root"
db='python_db'
conn=sql.connect(host=hosst,user=user,password=password,db=db)

cur=conn.cursor()

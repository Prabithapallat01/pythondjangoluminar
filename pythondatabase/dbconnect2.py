# step1. import mysql connector
import mysql.connector
#step2. establish aconnection with
db=mysql.connector.connect(
    host='localhost',
    user='root',
    port=3307,
    auth_plugin='mysql_native_password',
    passwd='Password@123',
    database='my_db'
)
cursor=db.cursor()
sql="create table movie(id int, m_name varchar(50),year varchar(50), rating int)"
cursor.execute(sql)
print("table created")
db.close()
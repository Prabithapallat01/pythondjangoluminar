import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    port=3307,
    auth_plugin='mysql_native_password',

    passwd='Password@123'
)
cursor=db.cursor()
sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    port=3307,
    auth_plugin='mysql_native_password',
    passwd='Password@123',
    database='my_db'
)
cursor=db.cursor()
try:
    sql="insert into movie values(101,'call wild',2020,4) "
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()
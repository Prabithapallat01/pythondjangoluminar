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
sql="select * from movie"
cursor.execute(sql)
movies=cursor.fetchall()
for movie in movies:
    print(movie)
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='test',
    auth_plugin='mysql_native_password'
)
# print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE runoob_db")
# mycursor.execute('show databases')
# for i in mycursor:
#     print(i)
mycursor.execute('select * from books')
myresult = mycursor.fetchall()  # 获取所有记录
for x in myresult:
    print(x)
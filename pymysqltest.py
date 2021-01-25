import pymysql  # PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库
db = pymysql.connect('localhost', 'root', 'root', 'test')
cursor = db.cursor()
cursor.execute('select * from books')
data = cursor.fetchall()
print(data)
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='tz_mysql',charset='utf8')

cur = conn.cursor()

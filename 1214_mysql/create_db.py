import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='')
cursor = conn.cursor() #傳回cursor物件
cursor.execute('SELECT VERSION()') #查詢版本
print('database version : %s' %(cursor.fetchall()))

sql = 'CREATE DATABASE IF NOT EXISTS testdb DEFAULT CHARSET=utf8'
print('SQL:',cursor.execute(sql))

conn.commit() #操作結果寫入資料庫
cursor.close() #關閉cursor物件
conn.close() #關閉connection物件
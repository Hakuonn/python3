import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='testdb',charset='utf8')
cursor = conn.cursor()

sql = 'SELECT * FROM users'
print('SQL select : ' , cursor.execute(sql))
# print(cursor.fetchmany(2))
print(cursor.fetchone())
cursor.close()
conn.close()
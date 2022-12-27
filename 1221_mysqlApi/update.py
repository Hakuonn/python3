import pymysql
conn = pymysql.connect(host='127.0.0.1' , user='root' , passwd='',db='testdb',charset='utf8')
cursor = conn.cursor()


sql = 'SELECT * FROM users'
print('sql select:',cursor.execute(sql))
print(cursor.fetchall()) #擷取紀錄集(all)

sql = "DELETE FROM users WHERE user_name='Tony'"
print('sql delete:',cursor.execute(sql))
conn.commit()

sql = 'SELECT * FROM users'
print('sql select:',cursor.execute(sql))
print(cursor.fetchall())
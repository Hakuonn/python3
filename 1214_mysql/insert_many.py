import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='testdb',charset='utf8')
cursor = conn.cursor()

#sql 指令裡VALUES都以%s來代表欄位值
sql = "INSERT INTO users(user_name,age,gender,email,password) VALUES(%s,%s,%s,%s,%s)"
cursor.executemany(sql,[('Peter','20','M','peter@gmail.com','1234'),
                        ('Wensday','25','F','wensday@gmail.com','3333'),
                        ('Emma','30','F','emma@gmail.com','1771')])
conn.commit() # 操作結果寫入資料庫

sql = 'SELECT * FROM users'
print('SQL select : ' , cursor.execute(sql))
print(cursor.fetchall())
cursor.close()
conn.close()

import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='testdb',charset='utf8')
cursor = conn.cursor()

sql = "INSERT INTO users(user_name,age,gender,email,password)\
    VALUES('Levy',18,'F','Levy@gamil.com','0000')"

print('SQL insert: ', cursor.execute(sql))
conn.commit() # 操作結果寫入資料庫

cursor.close()
conn.close()



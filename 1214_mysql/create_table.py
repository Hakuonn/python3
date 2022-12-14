import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='testdb',charset='utf8')
cursor = conn.cursor()

sql = 'CREATE TABLE IF NOT EXISTS users(id int(5) PRIMARY KEY AUTO_INCREMENT,\
    user_name VARCHAR(20),\
    age TINYINT(3),\
    gender CHAR(1),\
    email VARCHAR(80),\
    password VARCHAR(20))'

print('SQL : ', cursor.execute(sql))
conn.commit() # 操作結果寫入資料庫
conn.close()



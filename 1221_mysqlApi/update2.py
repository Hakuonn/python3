import pymysql
conn = pymysql.connect(host='localhost' , user='root' , passwd='',db='testdb',charset='utf8')
cursor = conn.cursor()

sql = "ALTER TABLE users ADD telephone CHAR(20)" #更新資料表
print('sql alter table', cursor.execute(sql))

sql = "ALTER TABLE users ADD city CHAR(20)"
print('sql alter table' , cursor.execute(sql))

sql = "SELECT * FROM users"
print('sql select:' , cursor.execute(sql))

sql = "INSERT INTO users(user_name) VALUES ('Lucy')"
print('sql insert:' , cursor.execute(sql))

sql = "SELECT * FROM users"
print('sql select:' , cursor.execute(sql))
conn.commit()
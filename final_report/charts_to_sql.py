#把排行榜列表傳入mysql

import pymysql
import json

conn = pymysql.connect(host='127.0.0.1' , user='root' , passwd='' , database='final' , charset='utf8mb4')
cursor = conn.cursor()

#新增table
sql = 'CREATE TABLE `final`.`charts` (`id` VARCHAR(30) NOT NULL , `title` VARCHAR(50) NOT NULL , `url` VARCHAR(200) NOT NULL , PRIMARY KEY (`id`));'
try:
    print('SQL : ' , cursor.execute(sql))
except:
    print('SQL:error')

#新增資料
with open('data/charts.json' , 'r') as f :
    charts = json.load(f)
sql = "INSERT INTO charts(id,title,url)VALUES(%s,%s,%s)"

try:
    for i in range(len(charts)):
        cursor.execute(sql,(charts[i]['id'],charts[i]['title'],charts[i]['url']))
    print('新增完成')
except:
    print('新增失敗')

conn.commit()
conn.close()
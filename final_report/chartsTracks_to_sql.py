#把每個排行榜的歌曲傳入mysql

import pymysql
import json
import music

conn = pymysql.connect(host='127.0.0.1' , user='root' , passwd='' , database='final' , charset='utf8mb4')
cursor = conn.cursor()

with open('data/charts.json' , 'r' , encoding='utf8') as f:
    charts = json.load(f)

#建立table
for tmp in range(len(charts)):
    sql = 'CREATE TABLE `%s` (`name` VARCHAR(300) NOT NULL , `url` VARCHAR(300) NOT NULL , `artist` VARCHAR(300) NOT NULL);'
    try:
        cursor.execute(sql,((charts[tmp]['title'])))
    except:
        print('SQL錯誤')


#在每個table建立資料
for tmp in range(len(charts)):
    tracks = music.get_charts_tracks('%s' %(charts[tmp]['id']))
    sql = "TRUNCATE TABLE `final`.`%s`"
    cursor.execute(sql,(charts[tmp]['title'])) #先清空資料表
    for i in range(len(tracks)):
        sql = "INSERT INTO `%s`(`name`,`url`,`artist`) VALUES (%s,%s,%s);"
        cursor.execute(sql , (charts[tmp]['title'],tracks[i]['name'],tracks[i]['url'],tracks[i]['artist']))

conn.commit()
conn.close()

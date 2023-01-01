import pymysql
import kkbox

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='kkbox',charset='utf8')
cursor = conn.cursor()
sql = "INSERT INTO charts(id,name,artist) VALUES(%s,%s,%s)"

# print(type(charts))
for chart in kkbox.get_charts_tracks("8o-CcG0PWzFpXs9omE"):
    cursor.execute(sql , (chart['id'] , chart['name'] ,chart['album']['artist']['name']))

conn.commit()

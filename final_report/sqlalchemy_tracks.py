#CURD tarcks
#查詢排行榜裡的歌曲
import sqlalchemy as db
import json


#查詢排行榜裡的歌曲(allfetch)
def select_charts(rankname):
    userName = 'root'
    passwd = ''
    host = '127.0.0.1'
    dbName = 'final'
    url = "mysql+pymysql://%s:%s@%s:3306/%s"%(userName,passwd,host,dbName)
    engine = db.create_engine(url)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table("'%s'"%(rankname) , metadata , autoload=True , autoload_with=engine)
    query = db.select([table]).order_by(db.desc(table.columns.artist))
    rows = connection.execute(query).fetchall()
    title = []
    for i in range(len(rows)):
        data = [rows[i][0] ,rows[i][1] ,rows[i][2]]
        title.append(data)
    # print(title)
    return title
# select_charts('我的最愛')



#更新排行榜裡歌曲的名稱
def update(ranktitle,update_name,song_url):
    userName = 'root'
    passwd = ''
    host = '127.0.0.1'
    dbName = 'final'
    url = "mysql+pymysql://%s:%s@%s:3306/%s"%(userName,passwd,host,dbName)
    engine = db.create_engine(url)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table("'%s'"%(ranktitle) , metadata , autoload=True , autoload_with=engine)
    query = db.update(table).values(name=update_name).where(table.columns.url==song_url)
    connection.execute(query)
    return '更新完成'


#刪除 
def delete(ranktitle,songname):
    userName = 'root'
    passwd = ''
    host = '127.0.0.1'
    dbName = 'final'
    url = "mysql+pymysql://%s:%s@%s:3306/%s"%(userName,passwd,host,dbName)
    engine = db.create_engine(url)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table("'%s'"%(ranktitle) , metadata , autoload=True , autoload_with=engine)
    query = db.delete(table).where(table.columns.name==songname)
    connection.execute(query)
    return '刪除完成'

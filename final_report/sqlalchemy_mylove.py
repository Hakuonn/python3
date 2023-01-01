#我的最愛(CURD)
import sqlalchemy as db

#查詢
def select_mylove():
    userName = 'root'
    passwd = ''
    host = '127.0.0.1'
    dbName = 'final'
    url = "mysql+pymysql://%s:%s@%s:3306/%s"%(userName,passwd,host,dbName)
    engine = db.create_engine(url)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table("'我的最愛'" , metadata , autoload=True , autoload_with=engine)
    query = db.select([table]).order_by(db.desc(table.columns.artist))
    rows = connection.execute(query).fetchall()
    title = []
    for i in range(len(rows)):
        data = [rows[i][0] ,rows[i][1] ,rows[i][2]]
        title.append(data)
    # print(title)
    return title
select_mylove()
#新增
def mylovesong(songname,songlink,artist):
    userName = 'root'
    passwd = ''
    host = '127.0.0.1'
    dbName = 'final'
    url = "mysql+pymysql://%s:%s@%s:3306/%s"%(userName,passwd,host,dbName)
    engine = db.create_engine(url)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table("'我的最愛'" , metadata , autoload=True , autoload_with=engine)
    query = db.insert(table).values(name=songname,url=songlink,artist=artist)
    connection.execute(query)
    return '已加入我的最愛'

#查詢排行榜名稱
import sqlalchemy as db

def select_charts():
    userName = 'root'
    passwd = ''
    host = '127.0.0.1'
    dbName = 'final'
    url = "mysql+pymysql://%s:%s@%s:3306/%s"%(userName,passwd,host,dbName)
    engine = db.create_engine(url)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table('charts' , metadata , autoload=True , autoload_with=engine)
    query = db.select([table]).order_by(db.desc(table.columns.id))
    rows = connection.execute(query).fetchall()
    title = []
    for i in range(15):
        data = [rows[i][0] ,rows[i][1] ,rows[i][2]]
        title.append(data)
    print(title)
    return title

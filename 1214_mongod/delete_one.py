import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

for i in mycol.find():
    print(i)
print()
col,va = input('輸入欄位與值(用空白分隔)').split(' ')
if col == '_id' or  col == 'age' :
    va = int(va)
myquery = {col:va}
print('刪除的資料:',myquery)
mycol.delete_one(myquery)
print()
for i in mycol.find():
    print(i)
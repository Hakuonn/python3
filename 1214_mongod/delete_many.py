import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

for i in mycol.find():
    print(i)
print()
col,va = input('輸入欄位與開頭英文字母(用空白分隔)').split(' ')
if col == '_id' or  col == 'age' :
    va = int(va)
myquery = {col:{'$regex':'^'+va}}
print('刪除的資料:',myquery)
mycol.delete_many(myquery)
print()
for i in mycol.find():
    print(i)
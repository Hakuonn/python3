import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['mydatabase']
mycol = mydb['customers']

for i in mycol.find():
    print(i)


col,va = input('輸入原欄位與資訊(用空白分隔)').split(' ')
new_col,new_va = input('輸入新欄位與資訊(用空白分隔)').split(' ')
if col == '_id' or  col == 'age' :
    va = int(va)
if new_col == '_id' or  new_col == 'age' :
    new_va = int(new_va)
myquery = {col:va}
newvalues = {"$set":{new_col:new_va}}

mycol.update_one(myquery,newvalues)
print()
print('-'*10)
print(myquery,'更改為',newvalues)
print('-'*10)
print()
for x in mycol.find():
    print(x)
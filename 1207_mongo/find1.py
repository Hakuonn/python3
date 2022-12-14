import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['customers']

print('-'*10,'find all','-'*10)
for x in mycol.find():
    print(x)

print('-'*10,'find name','-'*10)
myquery = {'name': 'Uber'}
for x in mycol.find(myquery):
    print(x)

print('-'*10,'find addr(gt)','-'*10)
myquery = {'address':{'$gt':'R'}} #字串比較大小會比較字串的第一個字
for y in mycol.find(myquery):
    print(y)

print('-'*10,'find name (regex)','-'*10)
myquery = {'name':{'$regex':'V'}} #regex 會列出字串中相符的字串
for z in mycol.find(myquery):
    print(z)


print('-'*10,'find addr (regex:^S)','-'*10)
myquery = {'address':{'$regex':'^S'}} #刪除S開頭的
for z in mycol.find(myquery):
    print(z)

#尋找某個字母開頭的資料
#addr
print('-'*10,'find addr (gt)','-'*10)
qaddr = '^' + input('Please input the addr you want to query:')
myquery = {'address':{'$regex':qaddr}}
for i in mycol.find(myquery):
    print(i)
#name
print('-'*10,'find name (gt)','-'*10)
qname = '^' + input('Please input the name you want to query:')
myquery = {'name':{'$regex':qname}}
for i in mycol.find(myquery):
    print(i)

print('-'*10,'find addr (lt)','-'*10)
qaddr = input('Please input the addr you want to query:')
myquery = {'address':{'$lt':qaddr}}
for i in mycol.find(myquery):
    print(i)

print('-'*10,'find age (gte)','-'*10)
qage = int(input('Please input the age you want to query:'))
myquery = {'age':{'$gte':qage}}
for i in mycol.find(myquery):
    print(i)

# >=30 and <=60
print('-'*10,'find age (or)','-'*10)
myquery = {'$and':[{'age':{'$lte':60}},{'age':{'$gte':30}}]}
for i in mycol.find(myquery):
    print(i)

#<20 or >65
print('-'*10,'find age (or)','-'*10)
myquery = {'$or':[{'age':{'$gt':65}},{'age':{'$lt':20}}]}
for i in mycol.find(myquery):
    print(i)


#排序(遞增預設1or不用寫,遞減-1)
qfield,qsort = input('要使用哪一個欄位、遞增(1)or遞減(-1)？(空格隔開)').split(' ')
mydoc = mycol.find().sort(qfield,int(qsort))
for i in mydoc:
    print(i)

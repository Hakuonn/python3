""" 單底線 """
# 1
for _ in range(2):
    print("hello world")

# 2
lang = ('python' , 'java' , 'c++')
name , _ , _ = lang
print(name)

""" 前單底線 """
# 1
class Prefix:
    def __init__(self):
        self.public = 1
        self._hopePrivate = 2

p = Prefix()
print(p.public)
print(p._hopePrivate)
p._hopePrivate = 3
print(p._hopePrivate)

# 2
from class_file_ex import *
print(publicFun())
print(_privateFun2())

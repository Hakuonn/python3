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
from mimetypes import init
from class_file_ex import *
print(publicFun())
print(_privateFun2())


""" 後單底線 """
# 1
def dummy(name , class_):
    pass


""" 前雙底線 """
# 1
class Dummy():
    def __init__(self):
        self.__baz = 3

d = Dummy()
print(dir(d))
# print(d.__baz)
print(d._Dummy__baz)

# 2
class subDummy(Dummy):
    def __init__(self):
        super().__init__()
        self.__baz = 333

sd = subDummy()
print(dir(sd))
print(sd._subDummy__baz)

""" 前後雙底線 """
class test:
    def __init__(self):
        self.foo = "hello"
        self._bar = "world"
t = test()
print(t)
print(t.foo + t._bar)
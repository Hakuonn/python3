""" 
單底線(_):
1.shell環境下代表最後一次執行結果
2.不重要的數值用單底線代替
3.保留變數的其中某個值
"""
# 暫時性或不重要的數
for _ in range(3):
    print('Hello World')

# 拆箱運算式
lang = ("python" ,"java" ,"c++")
name , _ , _ = lang
print(name)


""" 
前單底線:
1.類private的用法，希望此變數或函式僅供內部使用，但在Python中只是理想，仍能存取
2.前單底線函示，在from M import * 不會 import進來，除非指定import該函式 or 在__all__裡有定義
"""
# 1
class Prefix:
    def __init__(self):
        self.public = 1
        self._hopePrivate = 2

p = Prefix()
print(p.public)
print(p._hopePrivate) # 可讀取
p._hopePrivate = 3 #可重新賦予值
print(p._hopePrivate)

# 2
from class_file import *
from class_file import _privateFun #指定該函式才不會NameError
print(publicFun())
print(_privateFun()) #NameError
print(_privateFunc2())

""" 
後單底線:
1.需要把keyword當作變數名稱時，可在keyword字尾加單底線，即可正常運行
"""
def dummy(name,class_):
    pass



""" 
前雙底線:
1.python避免發生與子類別的變數名稱衝突，會對變數重新命名，稱為名稱修飾 -> _類別名__變數名
2.子類別也同時繼承父類別的屬性
"""
# 1
class Dummy():
    def __init__(self):
        self.__baz = 3

d = Dummy()
#print(d.__baz) # AttributeError 屬性錯誤
print(dir(d)) #dir() -> 查看物件裡目前所有屬性 #發現並沒有__baz屬性，最像的是_Dummy__baz屬性
print(d._Dummy__baz)

# 2
class subDummy(Dummy):
    def __init__(self):
        super().__init__()
        self.__baz = 33

sd = subDummy()
print(dir(sd)) #發現 繼承後的__baz 名稱被改為 _subDummy__baz
print(sd._Dummy__baz)
print(sd._subDummy__baz)

_specialDummy__baz = 99
class SpecialDummy:
    def test(self):
        return _specialDummy__baz

print(SpecialDummy().test())
sd = SpecialDummy()
print(dir(sd))


""" 
前後雙底線:
1.保留於特殊用途上，提供給使用者“複寫” ex: __init__
"""
class Dummy:
    def __init__(self):
        self.foo = "Hello"
        self._bar = 'World!'
d = Dummy()
print(d) #執行結果是記憶體裡的參考位置
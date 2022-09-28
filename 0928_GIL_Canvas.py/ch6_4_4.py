from random import random
import threading
import time
import queue
from numpy import random


def job(L, q):
    q.put(sum(L))


def multithreading(L):
    q = queue.Queue()
    s = 0
    for i in range(4):
        t = threading.Thread(target=job, args=(L, q))
        t.start()
        t.join()
        s += q.get()
    print('multithreading, sum:', s)


def normal(L):
    print("normal, sum:", sum(L))


# 主程式
L = list(range(1000000))

t = time.time()  # 抓取系統時間，以便待會計算函式運算所花費的時間
normal(L * 4)  # 傳入normal函式的List，內部的元素個數乘以四倍
print("normal cost time:", time.time()-t, "s\n")

t = time.time()
multithreading(L)
print("multithreading cost time:", time.time()-t, "s\n")

L = random.exponential(scale=1, size=1000000)
t = time.time()
multithreading(L)
print("numpy cost time:", time.time()-t, "s\n")

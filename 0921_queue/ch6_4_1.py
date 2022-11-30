""" 
佇列 Queue:多個執行緒之間通信or交換數據 -> 先進先出
堆疊 -> 先進後出
"""

from queue import Queue
from threading import Thread
import time


def send(Q):
    data = 1
    for i in range(10):
        print("t1 thread , send data to Queue", data, end="\n")
        Q.put(data)  # 將item放入佇列
        time.sleep(1)
        data += 1


def receive(Q):
    for i in range(10):
        data = Q.get()  # 將item取出
        print("t2 thread , receive data from Queue", data, end="\n")
        time.sleep(1)


Q = Queue()
t1 = Thread(target=send, args=(Q,))
t2 = Thread(target=receive, args=(Q,))

t1.start()
t2.start()

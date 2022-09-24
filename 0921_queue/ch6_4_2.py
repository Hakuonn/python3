""" 兩執行緒互相溝通 """

from queue import Queue
from threading import Thread
import time

def send(Q):
    data = 1
    for i in range(10):
        print('t1 Thread , send data to Queue' , data , "\n")
        Q.put(data)
        time.sleep(1)
        data+=1

def receive(Q):
    for i in range(10):
        data = Q.get()
        print('t2 Thread , receive data from Queue' , data , "\n")
        time.sleep(1)

Q = Queue()
t1 = Thread(target=send , args=(Q,)).start()
t2 = Thread(target=receive , args=(Q,)).start()

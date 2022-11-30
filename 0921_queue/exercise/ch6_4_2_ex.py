from threading import Thread
from queue import Queue
import time

def send(Q):
    data = 1
    for _ in range(10):
        print('t1 Thread , send data to Queue' , data , '\n')
        Q.put(data)
        data+=1
        time.sleep(1)

def receive(Q):
    for _ in range(10):
        print('t2 Thread , receive data from Queue' , Q.get() , '\n')

Q = Queue()
t1 = Thread(target=send , args=(Q,)).start()
t2 = Thread(target=receive , args=(Q,)).start()

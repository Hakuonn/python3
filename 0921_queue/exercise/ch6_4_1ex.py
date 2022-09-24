from queue import Queue
from threading import Thread
import time

def send(Q):
    data=1 
    for _ in range(10):
        print("t1 thread , send data to Queue" , data , end="\n")
        Q.put(data)
        time.sleep(1)
        data+=1

def receive(Q):
    for _ in range(10):
        data = Q.get()
        print("t2 thread , receive data from Queue" , data , "\n")
        time.sleep(1)
Q = Queue()
t1 = Thread(target = send , args=(Q,))
t2 = Thread(target = receive , args=(Q,))

t1.start()
t2.start()
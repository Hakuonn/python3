from random import random
import threading
import time
import queue
from numpy import random

def normal(L):
    print("normal,sum:",sum(L))


def job(L,q):
    q.put(sum(L))
def multithreading(L):
    q = queue.Queue()
    s = 0
    for i in range(4):
        t = threading.Thread(target=job,args=(L,q))
        t.start()
        t.join()
        s+=q.get()
        print('multithreading,sum:' , s)

L = list(range(10000))

#normal
t = time.time()
normal(L*4)
print("normal cost time:",time.time()-t ,"s\n")


#multithreading
t = time.time()
multithreading(L)
print('multithreading cost time:' , time.time()-t , 's\n')


#numpy
L = random.exponential(scale=1,size=10000)
t = time.time()
multithreading(L)
print("numpy cost time:" , time.time()-t , 's\n')
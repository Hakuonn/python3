import queue
import threading

def job(data,Q):
    for i in range(len(data)):
        data[i] **= 2
    Q.put(data)

def multithreading():
    Q = queue.Queue()
    data = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(3):
        t = threading.Thread(target=job , args=(data[i],Q))
        t.start()
        t.join()

    for i in range(3):
        print(Q.get())

multithreading()
print('finish')
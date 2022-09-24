import threading
import queue


def job(data, Q):
    for i in range(len(data)):
        data[i] **= 3
    Q.put(data)


def multithreading():
    Q = queue.Queue()
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

    for i in range(5):
        t = threading.Thread(target=job, args=(data[i], Q)) # args傳出的順序要與接收的參數對齊
        t.start()
        t.join()

    for i in range(5):
        print(Q.get())


multithreading()
print("finish")

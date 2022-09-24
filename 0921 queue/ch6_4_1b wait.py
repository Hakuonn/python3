import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting" + self.name)
        process_data(self.name, self.q)
        print("Exiting" + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)


users = ["user-1", "user-2", "user-3"]
usernames = ["name1", "name2", "name3", "name4", "name5",
             "name6", "name7", "name8", "name9", "name10"]
queueLock = threading.Lock()

""" 
FIFO(First in First Out,先進先出):queue.Queue(maxsize)
LIFO(Last in First Out,後近先出):queue.LifoQueue(maxsize)
優先級列隊:queue.PriorityQueue(maxsize)
# maxsize = 0 or maxsize < 0 代表隊列大小沒有限制
"""
workQueue = queue.Queue(10) # FIFO(First in First Out,先進先出)
threads = []
threadID = 1
# 創建新線程
for tName in users:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充隊列
queueLock.acquire()
for word in usernames:
    workQueue.put(word)
queueLock.release()

# 等待列隊清空
while not workQueue.empty():
    pass

# 通知線程是時候退出
exitFlag = 1

# 等待所有線程完成
for t in threads:
    t.join()
print("Exiting Main Thread")

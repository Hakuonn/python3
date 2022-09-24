import queue

#設置上限 maxsize = 10
q = queue.Queue(maxsize=10)

for i in range(100):
    if q.qsize() >= 10:
        #存放數據達到上限maxsize，插入會導致阻塞
        break
    else:
        q.put(i)

while not q.empty():
    n = q.get()
    print("本次取出數據：%s" %(n))




import queue


q = queue.Queue(maxsize=100)
for i in range(100):
    if q.qsize() >= 100:
        break
    else:
        q.put(i)

while not q.empty():
    n = q.get()
    print("本次提出數據：%d" %(n))
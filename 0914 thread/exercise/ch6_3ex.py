import threading
import time

def job1(num):
    print('job1 thread%s %s\n' %(num,time.ctime(time.time()))
    )
    time.sleep(1)
def job2(num):
    print('job2 thread%s %s\n' %(num,time.ctime(time.time()))
    )
    time.sleep(1)
def job3(num):
    print('job3 thread%s %s\n' %(num,time.ctime(time.time()))
    )
    time.sleep(1)

threads = []
threads.append(threading.Thread(target=job1,args=(1,)))
threads.append(threading.Thread(target=job2,args=(2,)))
threads.append(threading.Thread(target=job3,args=(3,)))
for i in range(len(threads)):
    threads[i].start()

str1 = "main thread"
for i in range(1,5):
    str2 = str1 + str(i) + '\n'
    print(str2)
    time.sleep(1)


for i in range(3):
    threads[i].join()

print('finish')
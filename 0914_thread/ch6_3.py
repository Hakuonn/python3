""" 6-3 多執行緒 """
""" 
建立多執行緒(使用列表管理多執行緒):
先建立List -> 用append加入List
"""




import threading
import time
def job1(num):
    print("job1 Thread%s%s\n" % (num, time.ctime(time.time())))  # ctime顯示系統時間
    time.sleep(1)


def job2(num):
    print("job2 Thread%s%s\n" % (num, time.ctime(time.time())))
    time.sleep(1)


threads = []  # 建立thread List 管理多執行緒 , 透過threads[i]啟動子執行緒
threads.append(threading.Thread(target=job1, args=(1,)))
threads[0].start()  # 透過threads[i]啟動子執行緒

threads.append(threading.Thread(target=job2, args=(2,)))
threads[1].start()


str1 = "Main Thread"
for i in range(1, 5):
    str2 = str1+str(i)+"\n"
    print(str2)
    time.sleep(1)

for i in range(2):
    threads[i].join()

print("finish")

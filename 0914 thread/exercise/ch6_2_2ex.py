import threading

def job(wear , wear1):
    print(wear + '\n')
    print(wear1 + '\n')

for i in range(3):
    print("main thread:" + str(i))

t = threading.Thread(target=job , kwargs={"wear":"net","wear1":"ok"})
t.start()
t.join()
print("Finish" , end='')
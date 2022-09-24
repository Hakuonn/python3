import threading
import time

def job():
    str1='Sub Thread:'
    str2=''
    for i in range(1,5):
        str2 = str1 + str(i) +'\n'
        print(str2)
        time.sleep(1)

t = threading.Thread(target=job)
t.start()

str1 = 'Main Thread:'
str2 = ''
for i in range(1,4):
    str2 = str1 + str(i) + "\n"
    print(str2)
    time.sleep(1)
t.join()
print("Finish~\n")
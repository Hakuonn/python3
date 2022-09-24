import threading
import time

def job(num):
    str1 = 'Sub thread:'
    str2 = ''
    for i in range(1,num):
        str2 = str1 + str(i) + '\n'
        print(str2)
        time.sleep(1)

num = 3
st = threading.Thread(target=job , args=(num,))

st.start()

str1 = 'Main Thread:'
str2 = ''
for i in range(1,3):
    str2 = str1 +str(i) +"\n"
    print(str2)
    time.sleep(1)

st.join()
print("finish")
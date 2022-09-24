""" 6-2 執行緒與參數 """
import threading
import time


def job(num):
    str1 = "Sub thread:"
    str2 = ""
    for i in range(1, num):
        str2 = str1 + str(i) + "\n"
        print(str2)
        time.sleep(1)


num = 3
st = threading.Thread(target=job, args=(num,))  # args -> 傳遞參數
""" 
args=(1,) 小括號後面要加逗號
args=[2] 中括號不需加
args={3} 大括號可加可不加
args={3,}
"""
st.start()

str1 = "Main Thread:"
str2 = ""
for i in range(1, 3):
    str2 = str1 + str(i) + "\n"
    print(str2)
    time.sleep(1)

st.join()
print("finish")

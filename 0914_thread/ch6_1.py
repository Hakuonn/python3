""" 6-1 單一執行序 """
""" 
Thread三步驟
1.引入threading
2.建立子執行緒
3.start()
"""

import threading
import time


def job():
    str1 = "Sub thread:"
    str2 = ""

    for i in range(1, 5):
        str2 = str1 + str(i) + "\n"
        print(str2)
        time.sleep(1)


st = threading.Thread(target=job)  # target -> 要執行的工作 or 副程式
st.start()  # 啟動子執行緒

str1 = "Main thread:"
str2 = ""
for i in range(1, 3):
    str2 = str1 + str(i) + "\n"
    print(str2)
    time.sleep(1)

st.join() #等到子執行緒執行結束後才繼續主程式運作
print("finish\n")

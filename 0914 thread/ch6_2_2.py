import threading


def job(wear, wear1, wear2):
    print(wear + "\n")
    print(wear1 + "\n")
    print(wear2)


for i in range(3):
    print("Main thread:" + str(i))

# 如果沒有用到其他therad程式，後面可以直接接.start()
t = threading.Thread(target=job, kwargs={
                     "wear": "uniqlo", "wear1": "planMe", "wear2": "NET"})
# 能用kwargs傳參數，但主要以args傳遞參數
t.start()
t.join()

print("Finsh", end="")

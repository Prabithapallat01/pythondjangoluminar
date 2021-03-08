import threading
import time
def display():
    for i in range(1,5):
        time.sleep(2)
        print("child thread executing")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()
begintime=time.time()
t.join()

for i in range(1,5):
    time.sleep(2)
    print("thread")
print(threading.currentThread().getName())
endtime=time.time()
total=endtime-begintime
print("total time=",total)



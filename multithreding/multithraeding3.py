from threading import *
import time
class Myclass:
    def job(self):
        for i in range(10):
            time.sleep(2)
            print("insie thread:")
obj=Myclass()

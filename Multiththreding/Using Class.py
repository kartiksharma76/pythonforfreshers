import threading

class MyThread(threading.Thread):
    def run(self):
        print("Thread using class")

t1 = MyThread()
t1.start()
t1.join()
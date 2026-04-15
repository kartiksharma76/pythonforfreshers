from queue import Queue

q = Queue()

def producer():
    q.put(10)

def consumer():
    print(q.get())
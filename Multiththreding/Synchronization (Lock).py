import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    lock.acquire()
    counter += 1
    lock.release()

threads = []

for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Counter:", counter)
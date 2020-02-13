"""
Mutex
    - Kind of lock. To allow only one thread accessible to the shared resource in a processor
    - How to use?
        - Lock mutex before editing the list (Lock.acquire())
        - After editing the list, release the mutex (Lock.release())
"""

from threading import Thread, Lock
import threading


def worker(mutex, data, thread_safe):
    if thread_safe:
        mutex.acquire()
    print("mutex status:", mutex.locked())

    try:
        # threading.get_ident(): return the thread id
        print(f"Thread {threading.get_ident()}: {data}\n")
    finally:
        if thread_safe:
            mutex.release()


if __name__ == "__main__":
    threads = []
    thread_safe = True
    mutex = Lock()  # use threading module's Lock to represent mutex
    for i in range(20):
        t = Thread(target=worker, args=(mutex, i, thread_safe))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

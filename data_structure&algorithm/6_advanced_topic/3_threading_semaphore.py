"""
Semaphore
    Semaphore's value is the number of threads which are accessible to a shared resource at once.
"""

import threading
import time


class ThreadPool(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def acquire(self, name):
        with self.lock:     # "with" does Lock.acquire() and Lock.release() automatically
            self.active.append(name)
            print(f"Acquired: {name} | Thread pool: {self.active}")

    def release(self, name):
        with self.lock:
            self.active.remove(name)
            print(f"Return: {name} | Thread pool: {self.active}")


def worker(semaphore, pool):
    with semaphore:
        name = threading.currentThread().getName()
        pool.acquire(name)
        time.sleep(1)
        pool.release(name)


if __name__ == "__main__":
    threads = []
    pool = ThreadPool()
    semaphore = threading.Semaphore(3)  # With this, line 39 is executed with three threads as a group (together / almost spontanteously)
    for i in range(10):
        t = threading.Thread(target=worker, name="Threadd " + str(i), args=(semaphore, pool))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


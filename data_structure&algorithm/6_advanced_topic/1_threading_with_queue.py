import queue_custom
import threading

q = queue_custom.Queue()


def worker(num):
    while True:
        item = q.get()
        if item is None:
            print(f"Thread {num + 1} is terminated")
            break
        # Handle the task
        print(f"Thread {num + 1}: process completed {item}")
        q.task_done()


if __name__ == "__main__":
    num_worker_threads = 10
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for item in range(20):
        q.put(item)

    # Block: Wait until all task is over (= wait until queue becomes empty)
    q.join()    # Queue.join(): Block until all items in the queue have been gotten and processed.

    # Stop: Terminate worker threads
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()    # Thread.join(): Wait until the thread terminates

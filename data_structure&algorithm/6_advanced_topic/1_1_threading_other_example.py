# From https://niceman.tistory.com/140
# An example of data transferring between threads

import threading
from queue_custom import Queue


def creator(data, q):
    print("Creating data and putting it on the queue")
    print("\n")
    for item in data:
        evt = threading.Event()     # host Event object
        """
            Event: for communication between threads: one thread signals an event and other threads wait for it.
        """
        q.put((item, evt))
        print("Waiting for data to be doubled")
        evt.wait()  # Call .wait() for synchronizing between threads


def consumer(q):
    while True:
        data, evt = q.get()
        print(f"Receive Original Data: {data}")
        processed = data * 5
        print(f"Receive Processed Data: {processed}")
        print("\n")
        evt.set()   # By calling .set(), the thread which has been "waited" starts working again.
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    data = [7, 14, 39, 59, 77, 1, 109, 99, 167, 928, 1035]
    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=consumer, args=(q,))
    thread_one.start()  # Without this, thread_two waits forever at q.get() line
    thread_two.start()  # Without this, thread_one waits forever at the first item to be consumed

    q.join()

    # # Stop: Terminate worker threads
    # q.put(None)
    # q.put(None)
    # thread_one.join()
    # thread_two.join()

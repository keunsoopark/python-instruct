# Producer/cosumer model with thread
# Condition object: https://docs.python.org/2/library/threading.html#condition-objects

import threading


def consumer(cond):
    name = threading.currentThread().getName()
    print(f"{name} Start")
    with cond:
        print(f"{name} Hold")
        cond.wait()     # Wait until notified
        print(f"{name} Consume resource")


def producer(cond):
    name = threading.currentThread().getName()
    print(f"{name} Start")
    with cond:
        print(f"{name} Notify all consumers after creating the resource")
        cond.notifyAll()    # Wake up all threads waiting on this condition


if __name__ == "__main__":
    condition = threading.Condition()

    consumer1_t = threading.Thread(name="consumer1", target=consumer, args=(condition,))
    consumer2_t = threading.Thread(name="consumer2", target=consumer, args=(condition,))

    producer_t = threading.Thread(name="producer", target=producer, args=(condition,))

    consumer1_t.start()
    consumer2_t.start()
    producer_t.start()

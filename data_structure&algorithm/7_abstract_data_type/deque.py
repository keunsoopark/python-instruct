# This code is also inefficient because of using .insert() and pop(0)
# -> Better way: check 6_1_collections_deque

from queue_custom import Queue


class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty.")


if __name__ == "__main__":
    deque = Deque()
    print(f"Deque is empty? {deque.isEmpty()}")
    print(f"Add numbers 0 - 9 in queue.")
    for i in range(10):
        deque.enqueue(i)
    print(f"Size of queue: {deque.size()}")
    print(f"peek: {deque.peek()}")
    print(f"dequeue: {deque.dequeue()}")
    print(f"peek: {deque.peek()}")
    print(f"Queue is empty? {deque.isEmpty()}")
    print()
    print(f"Deque: {deque}")
    print(f"dequeue: {deque.dequeue_front()}")
    print(f"peek: {deque.peek()}")
    print(f"Deque: {deque}")
    print("Run enqueue_back(50)")
    deque.enqueue_back(50)
    print(f"peek: {deque.peek()}")
    print(f"Deque: {deque}")

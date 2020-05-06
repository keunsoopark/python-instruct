# Implementation of Queue with List
# BUT, this is not a good implemenation because .insert() method moves all elements in the memory ~ O(n), instead of O(1)
# Implementation looks similar with 1_stack.py because .enqueue() is oppositely implemented with .push()


class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty.")

    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":
    queue = Queue()
    print(f"Queue is empty? {queue.isEmpty()}")
    print(f"Add numbers 0 - 9 in queue.")
    for i in range(10):
        queue.enqueue(i)
    print(f"Size of queue: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"Queue is empty? {queue.isEmpty()}")
    print(queue)

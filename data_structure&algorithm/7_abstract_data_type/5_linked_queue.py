# Use Node's container to represent Queue

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.pointer = None

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("Queue is empty.")

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            # since head and tail points the exact same object in memory
            # (Basically this is how head and tail are relevant each other in memory)
            # Check how this is working with setting up break points
            self.head = node
            self.tail = node
        else:
            if self.tail:
                # manipulating pointer of tail actually manipulates the pointer of head
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


if __name__ == "__main__":
    queue = Queue()
    print(f"Queue is empty? {queue.isEmpty()}")
    print(f"Add numbers 0 - 9 in queue.")
    for i in range(10):
        queue.enqueue(i)
    queue.print()

    print(f"Size of queue: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"Queue is empty? {queue.isEmpty()}")
    queue.print()

    print(queue.head.value)
    print(queue.head.pointer.value)
    print(f"dequeue: {queue.dequeue()}")
    print(queue.head.value)
    print(queue.head.pointer.value)
    print(f"dequeue: {queue.dequeue()}")
    print(queue.head.value)
    print(queue.head.pointer.value)
    queue.print()


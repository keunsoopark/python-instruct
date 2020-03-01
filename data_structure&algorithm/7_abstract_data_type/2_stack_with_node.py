# Use Node's container to represent Stack

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.head and self.count > 0:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print("Stack is empty.")

    def size(self):
        return self.count

    def peek(self):
        if self.head and self.count > 0:
            return self.head.value
        else:
            print("Stack is empty.")

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


if __name__ == "__main__":
    stack = Stack()
    print(f"Is stack empty? {stack.isEmpty()}")
    print(f"Adding 0-9 in stack...")
    for i in range(10):
        stack.push(i)
    print(f"Size of stack: {stack.size()}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"Is stack empty? {stack.isEmpty()}")
    stack._printList()

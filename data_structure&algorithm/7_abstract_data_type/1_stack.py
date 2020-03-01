# Use List to represent Stack

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty.")

    def __repr__(self):
        return repr(self.items)


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
    print(stack)

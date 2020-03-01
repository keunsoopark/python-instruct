# There is a capacity in Stack, and when it is full, it moves to next Stack

from stack import Stack


class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.set_of_stacks = []
        self.items = []
        self.capacity = capacity

    def push(self, value):
        if self.size() >= self.capacity:
            self.set_of_stacks.append(self.items)
            self.items = []
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            if self.set_of_stacks:
                self.items = self.set_of_stacks.pop()
                return self.items.pop()
            else:
                print("Stack is empty.")

    def size_stack(self):
        return self.size() + len(self.set_of_stacks) * self.capacity

    def __repr__(self):
        aux = []
        for s in self.set_of_stacks:
            aux.extend(s)
        aux.extend(self.items)
        return repr(aux)


if __name__ == "__main__":
    capacity = 5
    stack = SetOfStacks(capacity)
    print(f"Stack is empty? {stack.isEmpty()}")
    print(f"Add numbers 0-9 in stack")
    for i in range(10):
        stack.push(i)
    print(stack)
    print(f"Size of stack: {stack.size_stack()}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"Stack is empty? {stack.isEmpty()}")
    print(stack)

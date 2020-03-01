# To make the minimum value searchable with O(1)

from stack import Stack


class NodeWithMin(object):
    def __init__(self, value=None, minimum=None):
        self.value = value
        # self.minimum = minimum


class StackMin_kp(Stack):   # Tried to make sense but whatsoever, it does not make sense that Node contains its own minimum...
    def __init__(self):
        self.items = []
        self.minimum = None

    def push(self, item):
        if self.isEmpty():
            self.minimum = item
        elif item < self.minimum:
            self.minimum = item
        self.items.append(NodeWithMin(value=item))

    def pop(self):
        item = self.items.pop()
        if item is not None:
            if item.value == self.minimum:
                self.minimum = self._peekMinimum()
            return item.value
        else:
            print("Stack is empty.")

    def peek(self):
        if self.items:
            return self.items[-1].value
        else:
            print("Stack is empty.")

    def _peekMinimum(self):
        if self.minimum:
            return self.minimum
        else:
            print("Stack is empty.")

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.value)
        return repr(aux)


class StackMin_only_list(Stack):   # use pure list, without using NodeWithMin object
    def __init__(self):
        self.items = []
        self.minimum = None

    def push(self, item):
        if self.isEmpty():
            self.minimum = item
        elif item < self.minimum:
            self.minimum = item
        self.items.append(item)

    def pop(self):
        value = self.items.pop()
        if value is not None:
            if value == self.minimum:
                self.minimum = self._peekMinimum()
            return value
        else:
            print("Stack is empty.")

    def _peekMinimum(self):
        if self.minimum:
            return self.minimum
        else:
            print("Stack is empty.")

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i)
        return repr(aux)


if __name__ == "__main__":
    stack = StackMin_only_list()
    print("\n------- StackMin only list")
    print(f"Is Stack empty? {stack.isEmpty()}")
    print("Add number 10-1 and 1-4 in stack.")
    for i in range(10, 0, -1):
        stack.push(i)
    for i in range(1, 5):
        stack.push(i)
    print(stack)

    print(f"Stack size: {stack.size()}")
    print(f"peek: {stack.peek()}")
    print(f"_peekMinimum: {stack._peekMinimum()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"peeekMinimum: {stack._peekMinimum()}")
    print(f"Is Stack Empty? : {stack.isEmpty()}")
    print(stack)

    stack = StackMin_kp()
    print("\n------- StackMin kp")
    print(f"Is Stack empty? {stack.isEmpty()}")
    print("Add number 10-1 and 1-4 in stack.")
    for i in range(10, 0, -1):
        stack.push(i)
    for i in range(1, 5):
        stack.push(i)
    print(stack)

    print(f"Stack size: {stack.size()}")
    print(f"peek: {stack.peek()}")
    print(f"_peekMinimum: {stack._peekMinimum()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"peeekMinimum: {stack._peekMinimum()}")
    print(f"Is Stack Empty? : {stack.isEmpty()}")
    print(stack)

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newData):
        self.value = newData

    def setNext(self, newPointer):
        self.pointer = newPointer


if __name__ == "__main__":
    L = Node(value="a", pointer=Node(value="b", pointer=Node(value="c", pointer=Node(value="d"))))
    assert(L.pointer.pointer.value=="c")

    print(L.getData())
    print(L.getNext().getData())
    L.setData("aa")
    L.setNext(Node("e"))
    print(L.getData())
    print(L.getNext().getData())

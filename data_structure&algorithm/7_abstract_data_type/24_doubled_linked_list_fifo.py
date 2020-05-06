from linkedlistFIFO import LinkedListFIFO


class DNode(object):
    def __init__(self, value=None, pointer=None, previous=None):
        self.value = value
        self.pointer = pointer
        self.previous = previous


class DLinkedList(LinkedListFIFO):
    def printListInverse(self):
        node = self.tail
        while node:
            try:
                previous_value = node.previous.value
            except AttributeError:
                previous_value = None

            print(f"value: {node.value}, previous: {previous_value}")
            node = node.previous
        print()

    def _add(self, value):
        node = DNode(value)
        if self.length == 0:
            self.head = node
        else:
            self.tail.pointer = node
            node.previous = self.tail

        self.length += 1
        self.tail = node

    def _delete(self, node):
        self.length -= 1
        node.previous.pointer = node.pointer
        if not node.pointer:
            self.tail = node.previous

    def _find(self, index):
        node = self.head
        i = 0
        while node and i < index:
            node = node.pointer
            i += 1

        return node

    def deleteNode_kp(self, index):
        node = self._find(index=index)
        self._delete(node)

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, i = self._find(index)
            if i == index:
                self._delete(node)
            else:
                print(f"No node with index {index}")


if __name__ == "__main__":
    from collections import Counter

    ll = DLinkedList()
    for i in range(1, 5):
        ll._add(i)

    print("Linked list printing")
    ll.printList()
    print("Linked list reverse printing")
    ll.printListInverse()
    print("Add node whose value is 15, and print the linked list")
    ll.add(15)
    ll.printList()
    print("Delete all node, and print the linked list")
    for i in range(ll.length-1, -1, -1):
        print(i)
        ll.deleteNode_kp(index=i)
    ll.printList()

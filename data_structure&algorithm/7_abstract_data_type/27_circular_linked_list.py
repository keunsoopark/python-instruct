from linkedlistFIFO import LinkedListFIFO
from node import Node


class CircularLinkedListFIFO(LinkedListFIFO):
    def _add_kp(self, value):
        node = Node(value, self.head)   # new node's pointer is the linked list's head
        if self.length == 0:
            self.head = node
        else:
            self.tail.pointer = node

        self.length += 1
        self.tail = node

def isCircularll_kp(ll):
    if ll.length < 2:
        return False

    node = ll.head
    i = 0
    while node:
        if i > ll.length:
            return True
        node = node.pointer
        i += 1
    return False


def test_isCircularll():
    ll = LinkedListFIFO()
    for i in range(10):
        ll.add(i)
    assert(isCircularll_kp(ll) is False)

    lcirc = CircularLinkedListFIFO()
    for i in range(10):
        lcirc._add_kp(i)
    assert(isCircularll_kp(lcirc) is True)


if __name__ == "__main__":
    test_isCircularll()

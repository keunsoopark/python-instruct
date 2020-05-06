from linkedlistFIFO import LinkedListFIFO
from node import Node
from typing import List


def isPal(l1: List):
    if len(l1) < 2:
        return True
    if l1[0] != l1[-1]:
        return False
    return isPal(l1[1:-1])


def checkllPal_kp(ll: LinkedListFIFO):
    if ll.length < 2:
        return True

    first_node, _ = ll._find_by_index(0)
    last_node, _ = ll._find_by_index(ll.length-1)

    if first_node.value != last_node.value:
        return False

    ll.delete_node_by_index(0)
    ll.delete_node_by_index(ll.length-1)

    return checkllPal_kp(ll)


def checkllPal(ll:LinkedListFIFO):
    node = ll.head
    l = []

    while node is not None:
        l.append(node.value)
        node = node.pointer

    return isPal(l)


def test_checkllPal():
    ll = LinkedListFIFO()
    l1 = [1, 2, 3, 2, 1]
    for i in l1:
        ll.add(i)
    assert(checkllPal(ll) is True)

    ll.add(2)
    ll.add(3)
    assert(checkllPal(ll) is False)


if __name__ == "__main__":
    test_checkllPal()

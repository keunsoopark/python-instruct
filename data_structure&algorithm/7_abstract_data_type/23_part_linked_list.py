from linkedlistFIFO import LinkedListFIFO
from node import Node


def partList(ll, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()

    node = ll.head
    while node:
        if node.value > n:
            more.add(node.value)
        elif node.value < n:
            less.add(node.value)
        node = node.pointer

    less.add(n)
    more_node = more.head
    while more_node:
        less.add(more_node.value)
        more_node = more_node.pointer

    return less


if __name__ == "__main__":
    ll = LinkedListFIFO()
    l = [6, 7, 3, 4, 9, 5, 1, 2, 8]
    for i in l:
        ll.add(i)

    print("Before dividing:")
    ll.printList()

    print("After dividing:")
    newll = partList(ll, 6)
    newll.printList()

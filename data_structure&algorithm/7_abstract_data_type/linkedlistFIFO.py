# FIFO: (head)1->2->3->4(tail)
# Change the one from the book so that it can have the same structure with 10_linkedlist_LIFO.py

from node import Node


class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    # Print the valud of node from head
    def printList(self):
        node = self.head
        while node:
            try:
                pointer_value = node.pointer.value
            except AttributeError:
                pointer_value = None

            print(f"value: {node.value}, pointer: {pointer_value}")
            node = node.pointer
        print()

    def _delete(self, prev, node):
        self.length -= 1
        if not prev:  # delete head node
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    # Add new node at the first place (head)
    def _addFirst(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    # Add new node. If there is a tail, tail points the new node
    def _addNext(self, value):
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node
        self.length += 1

    # Add new node
    def add(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._addNext(value)

    # Find node by index
    def _find_by_index(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev

    # Find node by value
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # Delete node by index
    def delete_node_by_index(self, index):
        if index < self.length:
            node, prev = self._find_by_index(index)
            self._delete(prev=prev, node=node)
        else:
            print(f"Given index {index} is higher than the length of linked list")

    # Delete node by value
    def delete_node_by_value(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev=prev, node=node)
        else:
            print(f"There is no node having the given value {value}")


if __name__ == "__main__":
    ll = LinkedListFIFO()
    for i in range(1, 5):
        ll.add(i)
    print("Linked list print:")
    ll.printList()
    print("Delete node whose index is 2, and print the linked list:")
    ll.delete_node_by_index(2)
    ll.printList()
    print("Add a node whose value is 5, and print the linked list:")
    ll.add(15)
    ll.printList()
    print("Delete node whose value is 3, and print the linked list:")
    ll.delete_node_by_value(4)
    ll.printList()
    print("Delete all nodes, and print the linked list:")
    for i in range(ll.length-1, -1, -1):
        ll.delete_node_by_index(index=i)
    ll.printList()

# LIFO: (head)4->3->2->1

from node import Node


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None    # type: Node
        self.length = 0

    # print the value of head node
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

    # delete node based on the previous node
    def _delete(self, prev, node):
        self.length -= 1
        if not prev:    # delete head node
            self.head = node.pointer
            # self.head = self.head.pointer
        else:
            prev.pointer = node.pointer

    # Add new node. Point the head node as the next node, and the head points the new node
    def add(self, value):
        self.length += 1
        self.head = Node(value=value, pointer=self.head)

    def add_by_list(self, list):
        for elem in list:
            self.length += 1
            self.head = Node(value=elem, pointer=self.head)

    # Find node with index
    def _find_by_index(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev

    # Find node with value
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

    # Delete node whose index is given
    def delete_node_by_index(self, index):
        if index < self.length:
            node, prev = self._find_by_index(index)
            self._delete(prev=prev, node=node)
        else:
            print(f"Given index {index} is higher than the length of linked list")

    # Delete node whose value is given
    def delete_node_by_value(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev=prev, node=node)
        else:
            print(f"There is no node having the given value {value}")


if __name__ == "__main__":
    ll = LinkedListLIFO()
    for i in range(1, 5):
        ll.add(i)
    print("Linked list print:")
    ll.printList()
    print("Delete node whose index is 2, and print the linked list:")
    ll.delete_node_by_index(2)
    ll.printList()
    print("Delete node whose value is 3, and print the linked list:")
    ll.delete_node_by_value(3)
    ll.printList()
    print("Add node whose value is 15, and print the linked list:")
    ll.add(15)
    ll.printList()
    print("Delete all nodes, and print the linked list:")
    for i in range(ll.length-1, -1, -1):
        ll.delete_node_by_index(index=i)
    ll.printList()

    input_list = [2, 6, 4, 8, 7]
    ll_list = LinkedListLIFO()
    ll_list.add_by_list(input_list)
    ll_list.printList()

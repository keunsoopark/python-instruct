from linkedlistFIFO import LinkedListFIFO
from node import Node


class KthFromLast(LinkedListFIFO):
    def find_kth_to_last_kp(self, k):
        index = self.length - k
        node, _ = self._find_by_index(index=index)
        return node.value

    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head
        i = 0
        while p1:
            if i > k-1:
                try:
                    p2 = p2.pointer
                except AttributeError:
                    break
            p1 = p1.pointer
            i += 1
        return p2.value


if __name__ == "__main__":
    ll = KthFromLast()
    for i in range(1, 11):
        ll.add(i)
    print("Linked list:")
    ll.printList()
    k = 3
    k_from_last_kp = ll.find_kth_to_last_kp(k)
    print(f"kp_module: {k_from_last_kp} is {k}-th element from the last")
    k_from_last = ll.find_kth_to_last(k)
    print(f"book_module: {k_from_last} is {k}-th element from the last")

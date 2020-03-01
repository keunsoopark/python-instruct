# Here we use linked list to handle hash conflict

from linkedlistFIFO import LinkedListFIFO


class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        hashed_value = item % self.size
        return hashed_value

    def add(self, item):
        hashed_value = self._find(item)
        self.slots[hashed_value].add(value=item)

    def delete(self, item):
        hashed_value = self._find(item)
        self.slots[hashed_value].delete_node_by_value(value=item)

    def print(self):
        for i in range(self.size):
            print(f"Slow number {i}")
            self.slots[i].printList()


def test_hash_table():
    H1 = HashTableLL(3)
    for i in range(0, 20):
        H1.add(i)
    H1.print()
    print("\n Delete item 0, 1, 2")
    H1.delete(0)
    H1.delete(1)
    H1.delete(2)
    H1.print()


if __name__ == "__main__":
    test_hash_table()

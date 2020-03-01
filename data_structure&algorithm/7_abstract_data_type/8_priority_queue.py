# Implement PriorityQueue as using heapq

import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        print("item:", item)
        print("self._index:", self._index)
        print("priority:", priority)
        heapq.heappush(self._queue, (-priority, self._index, item))
        """
            >>> heap = []
            >>> data = [(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')]
            >>> for item in data:
            ...     heappush(heap, item)
            ...
            >>> while heap:
            ...     print(heappop(heap)[1])
            J
            O
            H
            N
        """
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name})"


def test_priority_queue():
    """ Both push and pop is O(logN) """
    q = PriorityQueue()
    q.push(Item("test1"), 1)
    q.push(Item("test2"), 4)
    q.push(Item("test3"), 3)
    assert(str(q.pop()) == "Item(test2)")
    print("Test passed!")


if __name__ == "__main__":
    test_priority_queue()



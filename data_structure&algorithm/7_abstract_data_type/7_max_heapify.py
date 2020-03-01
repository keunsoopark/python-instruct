# implement heap.heapify into code

class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        print("initial data:", self.data)
        # len(data) // 2: index of the left-bottom node
        for i in range(len(data) // 2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i & 1:   # &: bit-by-bit AND operation. In this case, it is identical with i % 2
            return i >> 1   # >>: binary right shift. In this case, it is identical with // 2
        else:
            return (i >> 1) - 1

    def left_child(self, i):
        return (i << 1) + 1
        # idx = i * 2 + 1
        # if idx > len(self.data):
        #     return None
        # return idx

    def right_child(self, i):
        return (i << 1) + 2

    def __max_heapify__(self, i):
        largest = i     # current node
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        # left child
        ## This line is "if cond then A else B" statement
        largest = (left < n and self.data[left] > self.data[largest]) and left or largest

        # right child
        largest = (right < n and self.data[right] > self.data[largest]) and right or largest

        # If current node is bigger than child, then Skip, else Swap
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            print(self.data)
            self.__max_heapify__(largest)

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]

        # Place the last node into the first node
        self.data[0] = self.data[n - 1]
        self.data = self.data[:n - 1]
        self.__max_heapify__(0)
        return max_element

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i != 0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)
        print(self.data)


def test_heapify():
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert (h.extract_max() == 8)
    h.insert(6)
    assert (h.extract_max() == 7)
    h.insert(100)
    assert (h.extract_max() == 100)
    print("Test passed!")


if __name__ == "__main__":
    test_heapify()

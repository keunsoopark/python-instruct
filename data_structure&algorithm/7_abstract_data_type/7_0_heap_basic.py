import heapq


def main():
    list1 = [4, 6, 8, 1]

    # Convert list to heap: O(n)
    heapq.heapify(list1)
    print(list1)

    # Insert an element in heap
    h = []
    heapq.heappush(h, (1, 'food'))
    heapq.heappush(h, (2, 'have fun'))
    heapq.heappush(h, (3, 'work'))
    heapq.heappush(h, (4, 'study'))
    print(h)

    # Delete an element -> delete the lowest one and return it
    list1 = [1, 4, 8, 6]
    print(heapq.heappop(list1))
    print(list1)

    # heappushpop: insert new element and delete the lowest one
    list1 = [1, 4, 8, 6]
    print(heapq.heappushpop(list1, 0))
    print(list1)

    # heapreplace: delete the lowest one and add new element
    list1 = [1, 4, 8, 6]
    print(heapq.heapreplace(list1, 0))
    print(list1)

    # merge: merge multiple objects and return a iterator
    for x in heapq.merge([1, 3, 5], [2, 4, 6]):
        print(x)


if __name__ == "__main__":
    main()

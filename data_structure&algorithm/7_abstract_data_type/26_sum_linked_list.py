from linkedlistFIFO import LinkedListFIFO
from node import Node


class LinkedListFIFOYield(LinkedListFIFO):
    def _printList(self):
        node = self.head
        while node:
            yield node.value
            node = node.pointer


def sumlls_kp(l1, l2):
    node = l1.head
    l1_num = 0
    i = 0
    while node:
        l1_num += node.value * pow(10, i)
        node = node.pointer
        i += 1

    node = l2.head
    l2_num = 0
    i = 0
    while node:
        l2_num += node.value * pow(10, i)
        node = node.pointer
        i += 1

    sum_num = str(l1_num + l2_num)
    sum_num = sum_num[::-1]
    lsum = LinkedListFIFOYield()
    for s in sum_num:
        lsum.add(s)

    return lsum


def sumlls(l1, l2):
    lsum = LinkedListFIFOYield()
    dig1 = l1.head
    dig2 = l2.head
    pointer = 0

    while dig1 and dig2:
        d1 = dig1.value
        d2 = dig2.value
        sum_d = d1 + d2 + pointer
        if sum_d > 9:
            pointer = sum_d / 10
            lsum.add(sum_d % 10)
        else:
            lsum.add(sum_d)
            pointer = 0
            dig1 = dig1.pointer
            dig2 = dig2.pointer

        if dig1:
            sum_d = pointer + dig1.value
            if sum_d > 9:
                lsum.add(sum_d % 10)
            else:
                lsum.add(sum_d)
            dig1 = dig1.pointer

        if dig2:
            sum_d = pointer + dig2.value
            if sum_d > 9:
                lsum.add(sum_d % 10)
            else:
                lsum.add(sum_d)
            dig2 = dig2.pointer

        return lsum


if __name__ == "__main__":
    l1 = LinkedListFIFOYield()
    l1.add(1)
    l1.add(7)
    l1.add(6)
    l1.add(2)

    l2 = LinkedListFIFOYield()
    l2.add(5)
    l2.add(5)
    l2.add(4)

    lsum = sumlls_kp(l1, l2)
    l = list(lsum._printList())
    for i in reversed(l):
        print(i, end="")
    print()

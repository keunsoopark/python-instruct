import string
import collections

from deque import Deque

STRIP = string.whitespace + string.punctuation + "\"'"


def palindrome_checker_with_deque_with_our_own_deque(str1):
    d1 = Deque()

    for s in str1.lower():
        if s not in STRIP:
            d1.enqueue(s)

    while d1.size() > 1:
        if d1.dequeue() != d1.dequeue_front():
            return False

    return True


def palindrome_checker_with_deque_with_collections_deque(str1):
    d2 = collections.deque()

    for s in str1.lower():
        if s not in STRIP:
            d2.append(s)

    while len(d2) > 1:
        if d2.pop() != d2.popleft():
            return False

    return True


if __name__ == "__main__":
    str1 = "Madam Im Adam"
    str2 = "Buffy is a Slayer"
    print(palindrome_checker_with_deque_with_our_own_deque(str1))
    print(palindrome_checker_with_deque_with_our_own_deque(str2))
    print(palindrome_checker_with_deque_with_collections_deque(str1))
    print(palindrome_checker_with_deque_with_collections_deque(str2))

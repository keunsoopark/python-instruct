from collections import Counter


def is_anagram(s1, s2):
    # use Counter, instead of normal dict
    counter_s1 = Counter()
    for c1 in s1:
        counter_s1[c1] += 1

    counter_s2 = Counter()
    for c2 in s2:
        counter_s2[c2] += 1

    if (counter_s1 - counter_s2) == Counter():
        return True
    return False

    # this is from book:
    # for i in (counter_s1 - counter_s2).values():
    #     if i:
    #         return False
    # return True


def test_is_anagram():
    s1 = "marina"
    s2 = "aniram"
    assert(is_anagram(s1, s2) is True)
    s1 = "google"
    s2 = "gouglo"
    assert(is_anagram(s1, s2) is False)


if __name__ == "__main__":
    test_is_anagram()
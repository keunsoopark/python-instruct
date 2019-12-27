from collections import Counter


def find_top_N_recurring_words(seq, N):
    dcounter = Counter()
    for word in seq.split():
        dcounter[word] += 1
    print(dcounter)
    return dcounter.most_common(N)


def test_find_top_N_recurring_words():
    seq = "buffy angier monster gender willo buffy monster super buffy angier"
    N = 3
    assert(find_top_N_recurring_words(seq, N) ==
           [("buffy", 3), ("angier", 2), ("monster", 2)])
    print("fib_generator passed!")


if __name__ == "__main__":
    test_find_top_N_recurring_words()

from collections import Counter, defaultdict


def find_dice_probabilities(S, n_faces=6):
    if S > 2 * n_faces or S < 2:
        return None

    cdict = Counter()
    ddict = defaultdict(list)

    # put all possibilities in dicts
    for dice1 in range(1, n_faces + 1):
        for dice2 in range(1, n_faces + 1):
            dice_sum = dice1 + dice2
            cdict[dice_sum] += 1
            ddict[dice_sum].append([dice1, dice2])

    return [cdict[S], ddict[S]]


def test_find_dice_probabilities():
    n_faces = 6
    S = 5
    results = find_dice_probabilities(S, n_faces)
    print(results)
    assert (results[0] == len(results[1]))
    print("fib_generator passed")


if __name__ == "__main__":
    test_find_dice_probabilities()

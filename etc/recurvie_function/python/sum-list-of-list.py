
numberAndArrayHell = [3, [1, 4, [3, [6, 2], 5], 1, 3], 4, [8, 1, [2, 1, 9], 5], 5, 9]


def resursive_deep(acc, array):
    if len(array) == 0:
        print("Total sum is {}".format(acc))
        return acc
    else:
        return resursive_deep(acc + (array[0] if isinstance(array[0], int) else resursive_deep(0, array[0])), array[1:])


resursive_deep(0, numberAndArrayHell)

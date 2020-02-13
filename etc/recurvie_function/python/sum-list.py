numbers = [3, 1, 4, 1, 5, 9]


def resursive(acc, array):
    if len(array) == 0:
        print("Total sum is {}".format(acc))
        return acc
    else:
        return resursive(acc + array[0], array[1:])


resursive(0, numbers)

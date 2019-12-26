def set_operations_with_dict():
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    d1 = dict(pairs)
    print("dictionary1\t: {0}".format(d1))

    d2 = {"a": 1, "c": 2, "d": 3, "e": 4}
    print("dictionary2\t: {0}".format(d2))

    intersection = d1.keys() & d2.keys()
    print("d1 n d2 (key)\t: {0}".format(intersection))
    print(type(d1.keys()))  # : class 'dict_keys', but still you can use the same methods in set

    intersection_items = d1.items() & d2.items()
    print("d1 n d2 (key,value\t: {0}".format(intersection_items))
    print(type(d1.items()))  # : class 'dict_items', but still you can use the same methods in set

    substraction1 = d1.keys() - d2.keys()
    print("d1 - d2 (key)\t: {0}".format(substraction1))

    substraction2 = d2.keys() - d1.keys()
    print("d2 - d1 (key)\t: {0}".format(substraction2))

    substraction_items = d1.items() - d2.items()
    print("d1 - d2 (key,value\t: {0}".format(substraction_items))

    # remove specific key in dict
    d3 = {key: d2[key] for key in d2.keys() - {"c", "d"}}
    print("d2 - {{c, d}}\t: {0}".format(d3))


if __name__ == "__main__":
    set_operations_with_dict()

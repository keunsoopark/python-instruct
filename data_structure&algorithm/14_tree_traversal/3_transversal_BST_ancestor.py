from transversal_BST_recursively import BSTwithTransversalRecursively


def find_ancestor(path, low_value, high_value):
    while path:
        current_value = path[0]
        if low_value <= current_value <= high_value:
            return current_value
        else:
            try:
                path = path[1:]
            except:
                return current_value


if __name__ == "__main__":
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)
    path = bst.preorder()
    print("Middle search: ", path)

    print("Common ancestor of 1 and 6:", find_ancestor(path, 1, 6))
    print("Common ancestor of 1 and 11:", find_ancestor(path, 1, 11))
    print("Common ancestor of 1 and 4:", find_ancestor(path, 1, 4))
    print("Common ancestor of 8 and 9:", find_ancestor(path, 8, 9))

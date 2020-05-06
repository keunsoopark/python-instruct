from binary_tree import NodeBT, BinaryTree


class Height(object):
    def __init__(self):
        self.height = 0


class NodeBST(NodeBT):
    def __init__(self, value=None, level=1):
        super().__init__(value=value,
                         level=level)

    def _add_next_node(self, value, level_here=2):
        new_node = NodeBST(value=value,
                           level=level_here)
        if value > self.value:
            if self.right:
                self.right = self.right._add_next_node(value=value,
                                                       level_here=level_here + 1)
            else:
                self.right = new_node
        elif value < self.value:
            if self.left:
                self.left = self.left._add_next_node(value=value,
                                                     level_here=level_here + 1)
            else:
                self.left = new_node
        else:
            raise Exception("Duplicated node is not allowed.")
        return self

    # def _search_for_node(self, value):


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
        # self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = NodeBST(value)
        else:
            self.root._add_next_node(value)


if __name__ == "__main__":
    bst = BinarySearchTree()
    # for i in range(1, 10):
    for i in [6, 4, 8, 2, 5, 7, 9, 1, 3]:
        bst.add_node(i)

    print("bt.is_leaf(8):", bst.is_leaf(8))
    print("bt.get_node_level(8):", bst.get_node_level(8))
    print("bt.is_root(10):", bst.is_root(10))
    print("bt.is_root(1)", bst.is_root(1))
    print("bt._get_height()", bst.get_height())
    print("bt.is_bst()", bst.is_bst())
    print("bt.is_balanced()", bst.is_balanced())

"""
    Binary search tree: https://mattlee.tistory.com/30
"""


class Height(object):
    def __init__(self):
        self.height = 0


class NodeBT(object):
    def __init__(self, value=None, level=1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    # def __repr__(self):
    #     return "{}".format(self.value)

    def __repr__(self, level=0):
        if self.value:
            ret = "\t"*level + repr(self.value) + "\n"
            if self.left:
                ret += self.left.__repr__(level + 1)
            if self.right:
                ret += self.right.__repr__(level + 1)
            return ret
        else:
            return None

    def _add_next_node(self, value, level_here=2):
        new_node = NodeBT(value=value,
                          level=level_here)
        if not self.value:
            self.value = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            # If there are children for both left and right sides, add new node on left side.
            self.left = self.left._add_next_node(value=value,
                                                 level_here=level_here + 1)
        return self

    def _search_for_node(self, value):
        if self.value == value:
            return self
        else:
            found = False
            if self.left:
                found = self.left._search_for_node(value)
            if self.right:
                found = found or self.right._search_for_node(value)
            return found

    def _is_leaf(self):
        return not self.right and not self.left

    def _get_max_height(self):
        # Find the maximum height from the node: O(n)
        heightr, heightl = 0, 0
        if self.right:
            heightr = self.right._get_max_height() + 1
        if self.left:
            heightl = self.left._get_max_height() + 1
        return max(heightr, heightl)

    def _is_bst_kp(self):
        # Figure out if it is binary search tree or not: O(n)
        if self.value:
            if self.right:
                if self.right.value <= self.value:
                    return False
                else:
                    self.right._is_bst()
            if self.left:
                if self.left.value >= self.value:
                    return False
                else:
                    self.left._is_bst()
            return True
        else:
            return True

    def _is_bst(self, left=None, right=None):
        # Figure out if it is binary search tree or not: O(n)
        if self.value:
            if left and self.value < left:
                return False
            if right and self.value > right:
                return False

            l, r = True, True
            if self.left:
                l = self.left._is_bst(left, self.value)
            if self.right:
                r = self.right._is_bst(self.value, right)
            return l and r
        else:
            return True

    def _is_balanced(self, height=Height()):
        # Figure out if it is balanced tree or not: O(n)
        lh = Height()
        rh = Height()

        if self.value is None:
            return True

        l, r = True, True
        if self.left:
            l = self.left._is_balanced(lh)
        if self.right:
            r = self.right._is_balanced(rh)

        height.height = max(lh.height, rh.height) + 1

        if abs(lh.height - rh.height) <= 1:
            return l and r

        return False


class BinaryTree(object):
    def __init__(self):
        self.root = None

    # def __repr__(self, level=0):
    #     if self.root:
    #         ret = "\t"*level + repr(self.root.value) + "\n"
    #         if self.root.left:
    #             ret += self.root.left.__repr__(level + 1)
    #         if self.root.right:
    #             ret += self.root.right.__repr__(level + 1)
    #         return ret
    #     else:
    #         return None

    def __repr__(self):
        return self.root.__repr__()

    def add_node(self, value):
        if not self.root:
            self.root = NodeBT(value)
        else:
            self.root._add_next_node(value)

    def is_leaf(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node._is_leaf()
        else:
            return False

    def get_node_level(self, value):
        node = self.root._search_for_node(value)
        if node:
            return node.level
        else:
            return False

    def is_root(self, value):
        return self.root.value == value

    def get_height(self):
        return self.root._get_max_height()

    def is_balanced(self):
        return self.root._is_balanced()

    def is_bst(self):       # bst: binary search tree
        return self.root._is_bst()


if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(1, 10):
        bt.add_node(i)
    print("bt.is_leaf(8):", bt.is_leaf(8))
    print("bt.get_node_level(8):", bt.get_node_level(8))
    print("bt.is_root(10):", bt.is_root(10))
    print("bt.is_root(1)", bt.is_root(1))
    print("bt._get_height()", bt.get_height())
    print("bt.is_bst()", bt.is_bst())
    print("bt.is_balanced()", bt.is_balanced())
    print(bt)

from binary_tree import NodeBT, BinaryTree


class NodeAVL(NodeBT):
    def __init__(self, value=None, height=1):
        super().__init__(value=value)
        self.height=height      # depreciate "level" and use "height" instead

    def insert(self, value):
        # 1) Insert node into binary search tree
        new_node = NodeAVL(value=value)
        if value < self.value:
            # self.left = self.left and self.left.insert(value) or new_node
            if self.left:
                self.left = self.left.insert(value=value)
            else:
                self.left = new_node
        elif value > self.value:
            # self.right = self.right and self.right.insert(value) or new_node
            if self.right:
                self.right = self.right.insert(value=value)
            else:
                self.right = new_node
        else:
            raise Exception("Duplicated node is not allowed.")

        # 2) Manipulate the heights in _rotate method
        return self._rotate(value)

    def _rotate(self, value):
        # 3) Update the height of parent's node
        self.height = 1 + max(self._get_height(self.left),
                              self._get_height(self.right))

        # 4) Balancing factor: left tree height - right tree height
        balance = self._get_balance()

        # 5) Rotate the tree as it is unbalanced
        if balance > 1:
            # Case 1: LL
            if value < self.left.value:
                return self._right_rotate()

            # Case 2: LR
            elif value > self.left.value:
                self.left = self.left._left_rotate()
                return self._right_rotate()

        elif balance < -1:
            # Case 3: RR
            if value > self.right.value:
                return self._left_rotate()

            # Case 4: RL
            elif value < self.right.value:
                self.right = self.right._right_rotate()
                return self._left_rotate()

        return self

    def _left_rotate(self):
        # Here self = y
        x = self.right
        T2 = x.left

        # Rotate
        x.left = self
        self.right = T2

        # Update the heights
        self.height = 1 + max(self._get_height(self.left),
                              self._get_height(self.right))
        x.height = 1 + max(self._get_height(x.left),
                           self._get_height(x.right))

        # Return new node
        return x

    def _right_rotate(self):
        # Here self = x
        y = self.left
        T2 = y.right

        # Rotate
        y.right = self
        self.left = T2

        # Update the heights
        self.height = 1 + max(self._get_height(self.left),
                              self._get_height(self.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        # Return new node
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self):
        return self._get_height(self.left) - self._get_height(self.right)

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node=node.left)

    def delete(self, value):
        if value < self.value:
            self.left = self.left.delete(value=value)
        elif value > self.value:
            self.right = self.right.delete(value=value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self._get_min_value_node(self.right)
            self.value = temp.value
            self.right = self.right.delete(node=temp.value)

        if self is None:
            return None

        return self._rotate(value=value)


class AVLTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if not self.root:
            self.root = NodeAVL(value=value)
        else:
            self.root = self.root.insert(value=value)

    def delete(self, value):
        self.root = self.root.delete(value)


def preorder(root):
    if root:
        print(f"({root.value}, {root.height-1})", end="")
        if root.left:
            preorder(root.left)
        if root.right:
            preorder(root.right)


if __name__ == "__main__":
    myTree = AVLTree()
    for i in range(10, 100, 10):
        myTree.insert(i)

    print("myTree.get_height()", myTree.get_height())
    print("myTree.is_bst()", myTree.is_bst())
    print("myTree.is_balanced()", myTree.is_balanced())
    preorder(myTree.root)
    print()

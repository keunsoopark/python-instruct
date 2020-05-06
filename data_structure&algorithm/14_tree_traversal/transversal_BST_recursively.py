from binary_search_tree import BinarySearchTree


class BSTwithTransversalRecursively(BinarySearchTree):
    def __init__(self):
        super().__init__()
        # self.root = None
        self.nodes_BFS = []
        self.nodes_pre = []
        self.nodes_post = []
        self.nodes_in = []

    def BFS(self):      # not recursive
        self.root.level = 1
        queue = [self.root]
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
            self.nodes_BFS.append(current_node.value)

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        return self.nodes_BFS

    def inorder(self, node=None, level=1):
        if self.root != 0:
            if not node and level == 1:
                node = self.root
            if node is None:
                return self.nodes_in
            self.inorder(node=node.left, level=level+1)
            self.nodes_in.append(node.value)
            self.inorder(node=node.right, level=level+1)
        return self.nodes_in

    def preorder(self, node=None, level=1):
        if self.root != 0:
            if not node and level == 1:
                node = self.root
            if node is None:
                return self.nodes_pre
            self.nodes_pre.append(node.value)
            self.preorder(node=node.left, level=level+1)
            self.preorder(node=node.right, level=level+1)
        return self.nodes_pre

    def postorder(self, node=None, level=1):
        if self.root != 0:
            if not node and level == 1:
                node = self.root
            if node is None:
                return self.nodes_post
            self.postorder(node=node.left, level=level+1)
            self.postorder(node=node.right, level=level+1)
            self.nodes_post.append(node.value)
        return self.nodes_post


if __name__ == "__main__":
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)

    print("bst.is_leaf(8)", bst.is_leaf(8))
    print("bst.get_node_level(8)", bst.get_node_level(8))
    print("bst.is_root(10)", bst.is_root(10))
    print("bst.is_root(1)", bst.is_root(1))
    print("bst.get_height()", bst.get_height())
    print("bst.is_bst()", bst.is_bst())
    print("bst.is_bst()", bst.is_bst())
    print("bst.is_balanced()", bst.is_balanced())

    print("bst.preorder()", bst.preorder())
    print("bst.postorder()", bst.postorder())
    print("bst.inorder()", bst.inorder())
    print("bst.BFS()", bst.BFS())

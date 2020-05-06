from collections import deque
from binary_search_tree import BinarySearchTree


class BSTwithTransversalIterative(BinarySearchTree):
    def inorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()       # stack: [10, 5, 3, 2, 1]
                nodes.append(current.value)
                current = current.right
        return nodes

    def preorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                nodes.append(current.value)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return nodes

    def preorder2(self):
        nodes = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                nodes.append(current.value)
                stack.append(current.right)
                stack.append(current.left)
        return nodes

    def postorder(self):
        current = self.root
        current_right = None
        nodes, stack, stack_right = [], [], []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if current.right:
                    current_right = current.right
                    while stack_right or current_right:
                        if current_right:
                            stack_right.append(current_right)
                            current_right = current_right.right
                        else:
                            current_right = stack_right.pop()
                            nodes.append(current_right.value)
                            current_right = current_right.left
                nodes.append(current.value)
                current = None
        return nodes

    def BFT(self):
        current = self.root
        nodes, queue = [], deque()
        queue.append(current)
        while queue:
            current = queue.popleft()
            nodes.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return nodes


if __name__ == "__main__":
    bst = BSTwithTransversalIterative()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)

    print("Node 8 is the leaf node?", bst.is_leaf(8))
    print("Level of node 8?", bst.get_node_level(8))
    print("Node 10 is the root node?", bst.is_root(10))
    print("Node 1 is the root node?", bst.is_root(1))
    print("The height is tree?", bst.get_height())
    print("Is it the binary search tree?", bst.is_bst())
    print("Is it the balanced tree?", bst.is_balanced())

    print("pre order traversal", bst.preorder())
    print("pre order traversal2", bst.preorder2())
    print("post order traversal", bst.postorder())
    print("in order traversal", bst.inorder())
    print("breath-first traversal", bst.BFT())

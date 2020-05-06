# pre-order traversal
def preorder(root):
    if root != 0:
        yield root.value
        if root.left:
            preorder(root.left)
        if root.right:
            preorder(root.right)


# post-order traversal
def postorder(root):
    if root != 0:
        if root.left:
            postorder(root.left)
        if root.right:
            postorder(root.right)
        yield root.value


# in-order traversal
def inorder(root):
    if root != 0:
        if root.left:
            inorder(root.left)
        yield root.value
        if root.right:
            inorder(root.right)

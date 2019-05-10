class BTNode:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def inorderGen(root):
    if root is None:
        return
    for item in inorderGen(root.left):
        yield item
    yield root.data
    for item in inorderGen(root.right):
        yield item


def tree_invert(root):
    if root is not None:
        root.left, root.right = root.right, root.left
        tree_invert(root.left)
        tree_invert(root.right)



root = BTNode(4)
root.left = BTNode(2, root)
root.left.left = BTNode(1, root.left)
root.left.right = BTNode(3, root.left)
root.right = BTNode(7, root)
root.right.left = BTNode(6, root.right)
root.right.right = BTNode(9, root.right)
for item in inorderGen(root):
    print(item,  end=" ")
print()
tree_invert(root)
for item in inorderGen(root):
    print(item,  end=" ")
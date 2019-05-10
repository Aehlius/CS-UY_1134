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
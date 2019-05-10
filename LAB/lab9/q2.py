import math


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
    if root.left is not None and root.right is not None:
        root.left, root.right = root.right, root.left
        tree_invert(root.left)
        tree_invert(root.right)
        return
    elif root.right is not None:
        root.left, root.right = root.right, None
        tree_invert(root.right)
        return
    elif root.left is not None :
        root.left, root.right = None, root.left
        tree_invert(root.left)
        return

'''
def is_bst(root, max_val=math.inf, min_val=-math.inf):
    if root.left is not None:
        if root.left.data < min_val or root.left.data > root.data:
            return False
        is_bst(root.left, root.data, min_val)
    if root.right is not None:
        if root.right.data > max_val or root.right.data < root.data:
            return False
        is_bst(root.right, max_val, root.data)
    if max_val == math.inf and min_val == -math.inf:
        return True
    return
'''

def is_bst(root, max_val=math.inf, min_val=-math.inf):
    if root is not None:
        if min_val < root.data < max_val:
            return is_bst(root.left, root.data, min_val) and is_bst(root.right, max_val, root.data)
        return False
    else:
        return True

if __name__ == '__main__':
    root = BTNode(6)
    root.left = BTNode(3, root)
    root.left.left = BTNode(1, root.left)
    root.left.right = BTNode(5, root.left)
    root.right = BTNode(11, root)
    root.right.left = BTNode(9, root.right)
    root.right.right = BTNode(15, root.right)
    print(is_bst(root))
    for item in inorderGen(root):
        print(item, end=" ")
    print()
    tree_invert(root)
    print()
    print(is_bst(root))
    for item in inorderGen(root):
        print(item, end=" ")
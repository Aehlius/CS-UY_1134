from BTNode import BTNode
from BTNode import inorderGen


def tree_duplicate(root, isRoot=True):
    if root is None:
        return
    if isRoot:
        tree = BTNode(root.data)
    else:
        tree = BTNode(root.data, root)
    left = root.left
    right = root.right
    tree.left = tree_duplicate(left, False)
    tree.right = tree_duplicate(right, False)
    return tree


def tree_duplicate(root):
    if root is None:
        return
    tree = BTNode(root.data)
    left = root.left
    right = root.right
    if root.left is not None:
        tree.left = tree_duplicate(left)
        tree.left.parent = tree
    if root.right is not None:
        tree.right = tree_duplicate(right)
        tree.right.parent = tree
    return tree


if __name__ == '__main__':
    root = BTNode(4)
    root.left = BTNode(2, root)
    root.left.left = BTNode(1, root.left)
    root.left.right = BTNode(3, root.left)
    root.right = BTNode(7, root)
    root.right.left = BTNode(6, root.right)
    root.right.right = BTNode(9, root.right)

    root_copy = tree_duplicate(root)
    for item in inorderGen(root_copy):
        print(item, end=" ")

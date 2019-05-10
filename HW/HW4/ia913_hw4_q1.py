import BST_complete


def min_subtree(subtree_root):
    # this function finds the minimum value of a BST
    if subtree_root.left is None and subtree_root.right is None:
        # if the node is a leaf, return it's value
        return subtree_root.data
    curr_min = subtree_root.data
    # otherwise compare the value of that node with it's children's min
    if subtree_root.left is not None:
        left_min = min_subtree(subtree_root.left)
        if curr_min > left_min:
            curr_min = left_min
    if subtree_root.right is not None:
        right_min = min_subtree(subtree_root.right)
        if curr_min > right_min:
            curr_min = right_min
    return curr_min


def max_subtree(subtree_root):
    # this function finds the maximum value of a BST
    if subtree_root.left is None and subtree_root.right is None:
        # if the node is a leaf, return it's value
        return subtree_root.data
    curr_max = subtree_root.data
    # otherwise compare the value of that node with it's children's min
    if subtree_root.left is not None:
        left_max = max_subtree(subtree_root.left)
        if curr_max < left_max:
            curr_max = left_max
    if subtree_root.right is not None:
        right_max = max_subtree(subtree_root.right)
        if curr_max < right_max:
            curr_max = right_max
    return curr_max


class Empty(Exception):
    pass


def min_and_max(tree_root):
    return (min_subtree(tree_root), max_subtree(tree_root))

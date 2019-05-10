import BST_complete


def leaves_list(root_node):
    if root_node.left is None and root_node.right is None:
        # if the node is a leaf, return it's value as a list
        return [root_node.data]
    elif root_node.left is not None and root_node.right is None:
        return leaves_list(root_node.left)
    elif root_node.left is None and root_node.right is not None:
        return leaves_list(root_node.right)
    else:
        left = leaves_list(root_node.left)
        right = leaves_list(root_node.right)
        # combine both lists in order to get a complete list
        return left + right

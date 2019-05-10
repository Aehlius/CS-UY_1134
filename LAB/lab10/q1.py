def single_left_rotation(self, node):
    parent = node.parent
    child = node.right
    t2 = child.left
    if parent is None:
        self.root = child
    elif node is parent.left:
        parent.left = child
    else:
        parent.right = child
    child.left = node
    node.parent = child
    node.right = t2
    if t2 is not None:
        t2.parent = node
    child.parent = parent


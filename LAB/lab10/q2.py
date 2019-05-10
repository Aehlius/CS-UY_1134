def recursive_insert(self, data, curr_root=None):
    if self.root is None:
        self.root = self.BTNode(data)
        self.size += 1
        return self.root
    if curr_root is None:
        curr_root = self.root
    if data <= curr_root.data:
        if curr_root.left is None:
            curr_root.left = self.BTNode(data, curr_root)
            self.size += 1
            return curr_root.left
        else:
            self.recursive_insert(data, curr_root.left)
    elif curr_root.right is None:
        curr_root.right = self.BTNode(data, curr_root)
        self.size += 1
        return curr_root.right
    else:
        self.recursive_insert(data, curr_root.right)


if __name__ == '__main__':
    bst = BST()
    for x in [5, 3, 8, 2, 7, 4, 9]:
        bst.recursive_insert(x)
        print("size:", len(bst))
    for item in bst:  print(item, end=' ')
    print()
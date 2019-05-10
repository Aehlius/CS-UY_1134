from BST_complete import BST


class BTNode:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def bst_same_set(bst1, bst2):
    if len(bst1) == len(bst2):
        lst1 = [0] * len(bst1)
        lst2 = [0] * len(bst2)
        count = 0
        for item1 in bst1:
            lst1[count] = item1
            count += 1
        count = 0
        for item2 in bst2:
            lst2[count] = item2
            count += 1
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
        return True
    return False


bst1 = BST()
for x in [15, 10, 5, 12, 20, 25]:
    bst1.insert(x)
bst2 = BST()
for x in [15, 12, 5, 10, 20, 25]:
    bst2.insert(x)
print(bst_same_set(bst1, bst2))
bst2.insert(30)
print(bst_same_set(bst1, bst2))




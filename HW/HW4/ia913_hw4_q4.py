import BST_complete


def create_chain_bst(n):
    # this function creates a degenerate tree with all right children from 1 to n
    chain_tree = BST_complete.BST()
    for i in range(n):
        # since the loop will insert larger values as it continues, all children will be right
        chain_tree.insert(i+1)
    return chain_tree


def add_items(bst, low, high):
    # this recursive function will add items in an order as to create a balanced tree
    mid = int((low+high)/2)
    if high <= low:
        bst.insert(mid)
    else:
        bst.insert(mid)
        add_items(bst, low, mid-1)
        add_items(bst, mid+1, high)


def create_complete_bst(n):
    # this function will create a balanced tree in range from 1 to n
    bst = BST_complete.BST()
    add_items(bst, 1, n)
    return bst


"""
The complexity for both algorithms is O(n), since the insert function
will insert every value from 1 to n only once, and perform a constant
amount of work in order to find the location of each item
I.e. every recursive call performs a constant amount of work
and there are a total of n recursive calls
Therefore, work is O(n) in both functions

"""
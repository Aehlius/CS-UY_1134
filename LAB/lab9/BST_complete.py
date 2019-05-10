#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Wed Jun 14 16:27:21 2017
Initially developed in class for 2017 Summer

Note that duplicates are allowed in the implementation.
  How hard would it be to make that an attribute of the tree?
  Interesting question.

@author: jsterling

"""

def inorder(root):
    if root is not None:
        for data in inorder(root.left): yield data
        yield root.data
        for data in inorder(root.right): yield data

def preorder(root):
    if root is not None:
        yield root.data
        for data in preorder(root.left): yield data
        for data in preorder(root.right): yield data

def postorder(root):
    if root is not None:
        for data in postorder(root.left): yield data
        for data in postorder(root.right): yield data
        yield root.data

class BST:
    class BTNode:
        def __init__(self, data=None, parent=None, left=None, right=None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def insert(self, data):
        """
        insert the data and return the new Node the will hold it
        """
        self.size += 1
        if self.root is None:
            self.root = self.BTNode(data)
            return self.root
        current = self.root
        while True: # Keep going till we have returned the new Node
            if data <= current.data: 
                if current.left is None: 
                    current.left = self.BTNode(data, current)
                    return current.left
                else: 
                    current = current.left
            # data > current.data
            elif current.right is None: 
                current.right = self.BTNode(data, current)
                return current.right
            else: 
                current = current.right

    def find(self, data):
        """
        Return the location of the data or None if not present
        """
        current = self.root
        while current:
            if data == current.data: 
                return current
            elif data <= current.data: 
                current = current.left
            else: 
                current = current.right
        return None
    
    def delete(self, data):
        target = self.find(data)
        # did they ask to delete something that isn't there?
        if target is None: 
            raise ValueError
        self.size -= 1
        # Is it a leaf? Then just get rid of it, after cleaning up the parent
        if target.left is None and target.right is None:
            # Was it the root? Then we have no root
            if target is self.root:
                self.root = None
            # Are we the left of right child? 
            # Our parent has to remove the correct child
            elif target.parent.left is target: 
                target.parent.left = None
            else: 
                target.parent.right = None
            # for gc set all of target's links to none
            target.parent = target.left = target.child = target.data = None
        # Just one child! replace the target node with its child
        elif target.left is None or target.right is None:
            child = target.left if target.left else target.right
            if target.parent is None:
                self.root = child
            if target.parent.left is target: 
                target.parent.left = child
            else: 
                target.parent.right = child
            # Connect the child to our parent. Ok if we were root.
            child.parent = target.parent
            # for gc set all of target's links to none
            target.parent = target.left = target.child = target.data = None
        else:
            # Has two children. We have a choice,replace its data with
            # the data from:
            # a) its "successor", i.e.the smallest descendent greater
            #    than it or 
            # b) its "predecessor", the largest descendent less than of equal
            #    to it.  
            # We will go with (b). Go down left and then as far right
            # as possible.
            # NB: we are not getting rid of the target node here, 
            # just replacing its data
            predecessor = target.left
            while predecessor.right is not None: 
                predecessor = predecessor.right
            # predecessor is now the node with the largest value <= target's
            # copy the data of the predecessor to the target
            target.data = predecessor.data
            # If the predecessor has a child it must be a left one, or
            # else the left one would have been the predecessor.
            child = predecessor.left  # may be None Replace
            # predecessor with its left child, changing it's parent
            if predecessor.parent.left is predecessor: 
                predecessor.parent.left = child
            else: 
                predecessor.parent.right = child
            if child is not None:
                child.parent = predecessor.parent
            # for the GC, set all of predecessor's fields to None
            # note that its right child is already None
            predecessor.parent = predecessor.left = predecessor.child = None

    def clear(self):
        self.root = None
        self.size = 0

    # Ok, this one's interesting. If we have written the traversal
    # functions right, could just loop through theirs.
    def __iter__(self, cur=None):
        if cur is None: cur = self.root
        if cur.left: 
            for item in self.__iter__(cur.left):
                yield item
        yield cur.data
        if cur.right: 
            for item in self.__iter__(cur.right):
                yield item
        #for item in inorder(self.root): yield item

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

    def recursive_insert(self, data, curr_root=None):
        if self.root is None and curr_root is None:
            self.root = self.BTNode(data)
            self.size += 1
            return self.root
        elif curr_root is None:
            curr_root = self.root
        if data <= curr_root.data:
            if curr_root.left is None:
                curr_root.left = self.BTNode(data, curr_root)
                self.size += 1
                return curr_root.left
            else:
                return self.recursive_insert(data, curr_root.left)
        elif curr_root.right is None:
            curr_root.right = self.BTNode(data, curr_root)
            self.size += 1
            return curr_root.right
        else:
            return self.recursive_insert(data, curr_root.right)


if __name__ == '__main__':
    bst = BST()
    for x in [5, 3, 8, 2, 7, 4, 9]:
        bst.recursive_insert(x)
        print("size:", len(bst))
    for item in bst:
        print(item, end=' ')
    print()
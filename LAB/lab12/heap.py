"""
heap.py

Array based implementation of a heap.

This file is a 'starter". Need to fill in add, remove, up_heap, and down_heap.
"""


class Heap:
    def __init__(self, data = None):
        """__init__: Set up an empty heap"""
        if data is None:
            self._data = []
            self._size = 0
        else:
            self._data = data
            self._size = len(data)
            self.heapify()

    def heapify(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1, -1):
            self.down_heap(j)

    def __len__(self):
        """__len__: Return the size of the heap"""
        return self._size

    def is_empty(self):
        """is_empty: Return True is the heap is empty and False otherwise"""
        return self._size == 0

    def min(self):
        """Return the 'smallest' value"""
        if self._size == 0: 
            raise KeyError('heap: min. empty heap')
        return self._data[0]        

    #
    # TODO
    #
    def add(self, value):
        """add value to the heap"""
        if self._size == len(self._data):
            self._data.append(value)
        else:
            self._data[self._size] = value
        self._size += 1
        self.up_heap(self._size - 1)


    def up_heap(self, index):
        """Bubble up the item at index, as needed"""
        parent = self._parent(index)
        while index != 0 and self._data[parent] > self._data[index]:
            self._swap(index, parent)
            index = parent
            parent = self._parent(parent)
    
    def remove_min(self):
        """Remove the smallest value"""
        if self._size == 0: 
            raise KeyError('heap: remove_min. empty heap')
        result = self._data[0]
        self._size -= 1
        self._data[0] = self._data[self._size]
        self._data[self._size] = None
        self.down_heap(0)
        return result

    def down_heap(self, index):
        """
        down_heap: 'Sift' the item at index down, as needed
        """
        while not self._is_leaf(index):
            min_child = self._left(index)
            if self._has_right(index):
                if self._data[self._right(index)] < self._data[min_child]:
                    min_child = self._right(index)
            if self._data[min_child] < self._data[index]:
                self._swap(min_child, index)
                index = min_child
            else:
                break

    #
    # Possibly convenient private methods
    #
    def _swap(self, i, j):
        """_Swap: swaps items at indices i and j"""
        self._data[i], self._data[j] = self._data[j], self._data[i]


    def _is_leaf(self, index):
        """_is_leaf: Is index a leaf? Check if it has a left child"""
        return not self._has_left(index)
        #return 2*index+1 > self._size - 1

    def _parent(self, index):
        """_parent: Returns parent's index, or zero if root?"""
        # Declaring the "root" its own parent, otherwise usual math
        return (index - 1) // 2 if index else 0

    def _has_left(self, index):
        """_has_left: Does index have a left child?"""
        return self._left(index) < len(self)

    def _left(self, index):
        """_left: Return index's left child's index assuming it exists"""
        return 2*index + 1

    def _has_right(self, index):
        """_has_right: Does index have a right child?"""
        return self._right(index) < len(self)

    def _right(self, index):
        """_right: Return index's right child's index assuming it exists"""
        return 2*index + 2




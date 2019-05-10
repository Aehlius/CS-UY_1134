"""
singlyLinked.py

Basics of a linked list.
No list class, just a Node type

Possible functions to write:
  list_print
  list_length
  list_add_tail
  list_add_head
"""


class Node:
    """
    Node: the basic object used for building linked lists.
    This version is for singly linked lists
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        pass


def list_print(L):
    if L is None:
        print('< >')
        return
    result = ['<']

    # while L.next is not None:
    node = L
    while node is not None:
        result.append(str(node.data))
        node = node.next

    result.append('>')
    print(' '.join(result))

def list_length(L):
    if L is None:
        return 0
    result = 0
    node = L
    while node is not None:
        result += 1
        node = node.next
    return result

def list_find_tail(L):
    if L is None:
        return None
    node = L
    # while node is not None:
    while node.next is not None:
        node = node.next
    return node

def list_add_tail(L, data):
    if L is None:
        L = Node(data)
    else:
        node = list_find_tail(L)
        node.next = Node(data)
    return L

def list_add_head(L, data):
    # saved_head = L
    # L = Node(data, saved_head)
    # L = Node(data, L)
    # L.next = saved_head
    # return L
    return Node(data, L)

def list_add_after(Prior, data):
    # remember the one after prior
    # saved_next = Prior.next
    # make the node and have prior point to it
    # Prior.next = Node(data)
    Prior.next = Node(data, Prior.next)
    # connect the new node to the old next node
    # Prior.next.next = saved_next

def list_remove_head(L):
    if L is None:
        return None
    return L.next

# question 1 code
def splice_list(L, spliceL, node):
    saved_ref = node.next
    node.next = spliceL
    spliceL_last = list_find_tail(spliceL)
    spliceL_last.next = saved_ref
    return L


class Empty(Exception):
    pass


class LinkedStack:

    def __init__(self):
        self._items = 0
        self.head = None

    def __len__(self):
        return self._items

    def is_empty(self):
        return self._items == 0

    def push(self, elem):
        saved_head = self.head
        self.head = Node(elem)
        self.head.next = saved_head
        self._items += 1

    def pop(self):
        if self.is_empty():
            raise Empty
        popped_node = self.head.data
        self.head = self.head.next
        self._items -= 1
        return popped_node

    def top(self):
        if self.is_empty():
            raise Empty
        return self.head

    def __str__(self):
        if self._items == 0:
            return '< >'
        result = ['<']

        # while L.next is not None:
        node = self.head
        while node.next is not None:
            result.append(str(node.data))
            node = node.next

        result.append('>')
        s = (' '.join(result))
        return s


if __name__ == '__main__':
    print('Linked List Stack Test Code\n\nPrinting an empty Stack')
    my_stack = LinkedStack()
    print(my_stack)
    print('Pushing to a stack')
    for i in range(1, 11):
        my_stack.push(i)
    print(my_stack)
    print('Popping from a stack')
    for i in range(5):
        my_stack.pop()
    print(my_stack)
    print('Finding length of stack')
    print(len(my_stack))
    for i in range(4):
        my_stack.pop()
    print('Printing a stack with a single item')
    print(my_stack)
    print('Creating a reference to top and printing its data')
    top_ref = my_stack.top()
    print(top_ref.data)
    print('Popping to create an empty stack')
    my_stack.pop()
    print(my_stack)
    #print('Popping an empty stack')
    #my_stack.pop()


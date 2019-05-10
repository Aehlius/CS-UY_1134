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

    #while L.next is not None:
    while L is not None:
        result.append(str(L.data))
        L = L.next

    result.append('>')
    print(' '.join(result))

def list_print(L):
    if L is None:
        print('< >')
        return
    result = ['<']

    #while L.next is not None:
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
    #while node is not None:
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
    #saved_head = L
    #L = Node(data, saved_head)
    #L = Node(data, L)
    #L.next = saved_head
    #return L
    return Node(data, L)

def list_add_after(Prior, data):
    # remember the one after prior
    #saved_next = Prior.next
    # make the node and have prior point to it
    #Prior.next = Node(data)
    Prior.next = Node(data, Prior.next)
    # connect the new node to the old next node
    #Prior.next.next = saved_next

def list_remove_head(L):
    if L is None:
        return None
    return L.next


# question 1 code
def splice_list(spliceL, node):
    saved_ref = node.next
    node.next = spliceL
    spliceL_last = list_find_tail(spliceL)
    spliceL_last.next = saved_ref
    # last_node = spliceL
    # while last_node.next is not None:
    #    last_node = last_node.next
    # last_node.next = saved_ref

if __name__ == '__main__':

    L = None
    list_print(L)
    #print(len(L))
    print(list_length(L))
    #L = Node(1)
    L = list_add_tail(L, 1)
    list_print(L)
    print(list_length(L))
    #print(L)
    #L.next = Node(4)
    L = list_add_tail(L, 4)
    list_print(L)
    print(list_length(L))
    #print(L)
    #L.next.next = Node(9)
    L = list_add_tail(L, 9)
    list_print(L)
    print(list_length(L))
    #print(L
    #L.next.next.next = Node(16)
    L = list_add_tail(L, 16)
    list_print(L)
    print(list_length(L))
    #print(L)
    print('<', L.data, L.next.data, L.next.next.data, L.next.next.next.data, '>')
    print(list_length(L))
    L = list_add_head(L, 64)
    list_print(L)
    L = list_remove_head(L)
    #list_remove_head(L)
    list_print(L)

    print('\n\nTest code problem 1\nList L')
    list_print(L)
    print('\nList Q')
    Q = None
    for i in range(5, 9):
        Q = list_add_tail(Q, i)
    list_print(Q)
    print('\nSpliced List at node value 4')
    splice_list(Q, L.next)
    list_print(L)
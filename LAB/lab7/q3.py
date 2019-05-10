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


# question 3

def print_lnk_lst(L):
    if L is None:
        return
    print(L.data, end =' ')
    print_lnk_lst(L.next)



def print_lnk_lst_reverse(L):
    if L is None:
        return
    print_lnk_lst_reverse(L.next)
    print(L.data, end=' ')


if __name__ == '__main__':

    print('\n\nTest code problem 3')
    print('\nList L')
    L = None
    for i in range(5):
        L = list_add_tail(L, i)
    list_print(L)
    print('\nPrinting list forward')
    print_lnk_lst(L)
    print('\nPrinting list backwards')
    print_lnk_lst_reverse(L)

class DNode:
    def __init__(self, data=None, next=None, prior=None):
        self.data = data
        self.next = next
        self.prior = prior

class DLL:
    def __init__(self):
        self._header = DNode()
        self._trailer = DNode()
        self._size = 0
        self._header.next = self._trailer
        self._trailer.prior = self._header

    def add_head(self, value):
        new_node = DNode(value)
        new_node.prior = self._header
        new_node.next = self._header.next
        self._header.next.prior = new_node
        self._header.next = new_node
        self._size += 1

    def __str__(self):
        result = ""
        cursor = self._header.next
        while cursor is not self._trailer:
            result += str(cursor.data) + " "
            cursor = cursor.next
        return result

'''
def reverse_lnk_lst(lnk_lst):
    cursor = lnk_lst._trailer.prior.prior
    for i in range(lnk_lst._size-1):
        last_node = lnk_lst._trailer.prior
        prev_node = cursor.prior
        next_node = cursor.next
        last_node.next.prev = cursor
        cursor.next = last_node.next
        cursor.prior = last_node
        last_node.next = cursor
        prev_node.next = next_node
        next_node.prior = prev_node
        cursor = prev_node
    first_node = lnk_lst._header.next
    lnk_lst._header.next = first_node.next
    first_node.next.prior = lnk_lst._header
    first_node.next = lnk_lst._trailer
    '''


def reverse_lnk_lst(lnk_lst):
    header = lnk_lst._header
    trailer = lnk_lst._trailer
    cursor = header.next
    while cursor != trailer:
        cursor.next, cursor.prior = cursor.prior, cursor.next
        cursor = cursor.prior
    trailer.prior, header.next = header.next, trailer.prior
    header.next.prior = header
    trailer.prior.next = trailer


if __name__ == '__main__':
    dll = DLL()
    dll.add_head(1)
    dll.add_head(2)
    dll.add_head(3)
    dll.add_head(4)
    dll.add_head(5)


    print(dll)

    reverse_lnk_lst(dll)
    print(dll)

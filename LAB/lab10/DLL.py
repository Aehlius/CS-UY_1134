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

    def add_tail(self, value):
        new_node = DNode(value)
        self._trailer.prior.next = new_node
        new_node.prior = self._trailer.prior
        new_node.next = self._trailer
        self._trailer.prior = new_node
        self._size += 1

    def __str__(self):
        result = ""
        cursor = self._header.next
        while cursor is not self._trailer:
            result += str(cursor.data) + " "
            cursor = cursor.next
        return "< " + result + ">"


class SetOA:

    _AVAIL = object()

    def __init__(self):
        self._size = 0
        self._table = [None] * 10

    def _slot(self, key):
        return hash(key) % len(self._table)

    def __len__(self):
        return self._size

    def _resize(self, n):
        table = self._table
        self._table = [None] * int(n * len(table))
        self._size = 0

        for key in table:
            if key is not None and key != self._AVAIL:
                self.add(key)

    def add(self, key):
        slot = self._slot(key)
        avail_slot = None
        while self._table[slot] is not None:
            if self._table[slot] == self._AVAIL and avail_slot is None:
                avail_slot = slot
            slot += 1
            slot %= len(self._table)
        if avail_slot is not None:
            self._table[avail_slot] = key
        else:
            self._table[slot] = key
        self._size += 1
        if self._size > len(self._table) * 0.5:
            self._resize(2)
        return True

    def remove(self, key):
        slot = self._slot(key)
        while self._table[slot] is not None:
            if self._table[slot] == key:
                self._table[slot] = self._AVAIL
                self._size -= 1
                if self._size < len(self._table) * 0.25:
                    self._resize(.5)
                return
            slot += 1
            slot %= len(self._table)
        raise KeyError('Key error for the key:', str(key))

    def __iter__(self):
        for item in self._table:
            if item is not None and item != self._AVAIL:
                yield item

    def __contains__(self, key):
        slot = self._slot(key)
        check_count = 0
        while self._table[slot] is not None:
            if self._table[slot] == key:
                return True
            slot += 1
            slot %= len(self._table)
            check_count += 1
            if check_count > len(self._table):
                break
        return False


if __name__ == '__main__':
    my_set = SetOA()
    for i in range(50):
        my_set.add(i * 2)

    print("size", len(my_set))
    print("table size", len(my_set._table))

    for item in my_set:
        print(item, end=' ')
    print()
    for i in range(20):
        my_set.remove(i * 2)

    print("size", len(my_set))
    print("table size", len(my_set._table))

    for item in my_set:
        print(item, end=' ')
    print()
    for val in my_set._table:
        print(val, end=" ")
    print()
# The following class has been copied from NYU Classes
class SetHT:

    def __init__(self, init_size=10):
        self._table = [ [] for i in range(init_size) ]
        self._size = 0

    def add(self, value):
        # where do we add it?
        bucket = self._bucket(value)
        for item in bucket:
            if item == value:
                return False
        bucket.append(value)
        self._size += 1
        if self._size >= len(self._table) * 0.9:
            self._resize(2)
        return True

    def remove(self, value):
        bucket = self._bucket(value)
        for index in range(len(bucket)):
            if bucket[index] == value:
                bucket[index] = bucket[-1]
                bucket.pop()
                self._size -= 1
                return
        raise KeyError('Key Error for set:' + str(value))

    def __contains__(self, value):
        bucket = self._bucket(value)
        for item in bucket:
            if item == value:
                return True
        return False


    def __iter__(self):
        pass

    def __len__(self):
        return self._size

    def _bucket(self, value):
        return  self._table[hash(value) % len(self._table)]

    def _resize(self, n):
        table = self._table #remember
        self._size = 0
        self._table = [[] for i in range(n)]

        for bucket in table:
            for item in bucket:
                self.add(item)


# problem 4 code

def intersection_list(lst1, lst2):
    num_hash = SetHT()
    output_lst = []
    for num in lst1:
        num_hash.add(num)
    for num in lst2:
        if num in num_hash:
            # uses contains method to find if num in lst2 is in lst1
            # runs under close to constant runtime if minimal collisions
            output_lst.append(num)
    return output_lst


if __name__ == '__main__':
    lst1 = [3, 9, 2, 7, 1]
    lst2 = [4, 1, 8, 2]
    print(intersection_list(lst1, lst2))
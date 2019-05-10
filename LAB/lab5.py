# problem 1


import ctypes


class DynArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = self._make_array_(self.capacity)

    def __len__(self):
        return self.size

    def __str__(self):
        result = '['
        for i in range(self.size):
            result += str(self.data[i]) + ','
        result = result[:-1]
        #result[-1] = ']'
        return result + ']'

    def __str__(self):
        return '[' + ','.join([str(self.data[index])
                        for index in range(self.size)]) + ']'

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        self.data[self.size] = item
        self.size += 1

    def __getitem__(self, index):
        if index >= 0:
            if index >= self.size:
                raise IndexError
            return self.data[index]
        else:
            if -index > self.size:
                raise IndexError
            return self.data[self.size+index]

    def __setitem__(self, index, item):
        self.data[index] = item

    def _make_array_(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self, capacity):
        # create new array
        old_data = self.data
        self.data = self._make_array_(capacity)
        # copy values from old to new
        for index in range(self.size):
            self.data[index] = old_data[index]
        # update the capacity
        self.capacity = capacity
        # make sure our data field refers the new array

    def pop(self, index=None):
        if index is None:
            item = self[-1]
            self[-1] = None
            self.size -= 1
        else:
            if index < 0:
                index = self.size + index + 1
            item = self[index]
            for i in range(index, self.size-1):
                self[i] = self[i+1]
            self[-1] = None
            self.size -= 1
        return item

    def __add__(self, other):
        total_length = len(self)+len(other)
        totalArray = DynArray()
        totalArray._resize(total_length)
        for i in range(len(self)):
            totalArray.append(self[i])
        for i in range(len(other)):
            totalArray.append(other[i])
        return totalArray

    def __iadd__(self, other):
        self._resize(self.size+other.size)
        for i in range(len(other)):
            self.append(other[i])
        return self

    def extend(self, other):
        return self.__iadd__(other)

    def __mul__(self, multiplier):
        resultArray = DynArray()
        resultArray._resize(len(self)*multiplier)
        for i in range(len(self)*multiplier):
            resultArray.append(self[i % self.size])
        return resultArray

    def __rmul__(self, multiplier):
        resultArray = DynArray()
        resultArray._resize(len(self) * multiplier)
        for i in range(len(self) * multiplier):
            resultArray.append(self[i % self.size])
        return resultArray

# problem 2


print('\n\nTowers of Hanoi - number of moves\n')


def towers(n, start, target, helper):
    if n >= 1:
        moves_before = towers(n-1, start, helper, target)
        moves_after = towers(n-1, helper, target, start)
        total_moves = moves_before + moves_after + 1
        return total_moves
    else:
        return 0


for i in range(11):
    print('Total for', i, 'discs:', towers(i, 'A', 'C', 'B'), 'moves')


# test code

if __name__ == '__main__':
    print('\nDynamic Array\n')
    myArray = DynArray()
    myArray2 = DynArray()
    for i in range(5):
        myArray.append(i)
    for i in range(5, 10):
        myArray2.append(i)

    print('The original arrays')
    print(myArray)
    print(myArray2)
    print('\nIndexing')
    print(myArray[4])
    print(myArray[-2])

    print('\nPopping')
    print(myArray)
    myArray.pop()
    print(myArray)
    myArray.pop(-2)
    print(myArray)
    myArray.pop(2)
    print(myArray)

    print('\nAdding')
    print(myArray+myArray2)
    myArray += myArray2
    print(myArray)
    print(myArray.extend(myArray2))

    print('\nMultiplying')
    print(myArray)

    print(myArray*3)
    print(3*myArray)

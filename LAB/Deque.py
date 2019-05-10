class Full(Exception):
    pass

class Empty(Exception):
    pass

class Deque:
    def __init__(self, n):
        self.data = [None] * n
        self.size = 0
        self.front = 0
        self.back = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return '<' + ','.join([str(self.data[(i + self.front) % len(self.data)]) for i in range(self.size)]) + '>'

    def add_last(self, item):
        if self.size == len(self.data):
            raise Full
        self.data[self.back] = item
        self.back += 1
        if self.back == len(self.data):
            self.back = 0
        #self.back = (self.back + 1) % len(self.data)
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            raise Empty
        result = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return result

    def add_first(self, item):
        if self.size == len(self.data):
            raise Full
        self.data[self.front-1] = item
        self.front -= 1
        if self.front < 0:
            self.front = len(self.data)-1
        self.size += 1

    def delete_last(self):
        if self.size == 0:
            raise Empty
        result = self.data[self.back-1]
        self.data[self.back] = None
        self.back = (self.back - 1) % len(self.data)
        self.size -= 1
        return result


# test code

if __name__ == '__main__':
    dq = Deque(10)
    lst_dq = []
    print('Adding to the back of the queue')
    for i in range(5):
        dq.add_last(i)
        print(dq)
    print('Adding to the front of the queue wrapping around')
    for i in range(-1, -6, -1):
        dq.add_first(i)
        print(dq)
    print('Deleting from the front of the queue')
    for i in range(5):
        lst_dq.append(dq.delete_first())
        print(dq)
    print('Deleting from the front of the queue wrapping around')
    for i in range(4):
        lst_dq.append(dq.delete_first())
        print(dq)
    print('Adding to the back of the queue wrapping around')
    for i in range(5, 12):
        dq.add_last(i)
        print(dq)
    print('Deleting from the back of the queue wrapping around')
    for i in range(6):
        lst_dq.append(dq.delete_last())
        print(dq)
print('List of returned values')
print(lst_dq)
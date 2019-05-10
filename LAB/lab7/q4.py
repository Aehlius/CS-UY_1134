class Empty(Exception):
    pass

class Queue:
    def __init__(self, n):
        self.data = [None] * n
        self.size = 0
        self.front = 0
        self.back = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return '<' + ','.join([str(self.data[(i + self.front) % len(self.data)]) for i in range(self.size)]) + '>'


    def grow_queue(self):
        ref_lst = [None] * self.size*2
        for i in range(self.size):
            ref_lst[i] = self.data[(self.front + i) % self.size]
        self.front = 0
        self.back = self.size
        self.data = ref_lst


    def enqueue(self, item):
        if self.size == len(self.data):
            self.grow_queue()
        self.data[self.back] = item
        self.back += 1
        if self.back == len(self.data):
            self.back = 0
        #self.back = (self.back + 1) % len(self.data)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Empty
        result = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return result


if __name__ == '__main__':
    print('Problem 4 Test Code\n\nTest queue')
    my_queue = Queue(5)
    for i in range(5):
        my_queue.enqueue(i)
    print(my_queue)
    print('Test queue capacity')
    print(len(my_queue.data))
    print('Test queue at full capacity\n\nAdd another value')
    my_queue.enqueue(5)
    print(my_queue)
    print('New test queue capacity')
    print(len(my_queue.data))

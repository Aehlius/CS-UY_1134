from heap import Heap


class Empty(Exception):
    pass


class Queue:
    def __init__(self):
        self.size = 0
        self.priority = 0
        self.data = Heap()

    def enqueue(self, elem):
        elem_priority = (self.priority, elem)
        self.data.add(elem_priority)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty
        elem_tuple = Heap.remove_min(self.data)
        self.size -= 1
        return elem_tuple[1]

    def first(self):
        if self.is_empty():
            raise Empty
        elem_tuple = Heap.min(self.data)
        return elem_tuple[1]

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    q = Queue()
    for i in range(5,0,-1):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())
        print(q.first())

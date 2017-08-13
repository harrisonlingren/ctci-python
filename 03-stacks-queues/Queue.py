class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def dequeue(self):
        if self.first is None:
            return None
        old = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.size -= 1
        return old

    def enqueue(self, val):
        new = Node(val)
        if self.last != None:
            self.last.next = new
        self.last = new
        if self.first is None:
            self.first = self.last
        self.size += 1

    def peek(self):
        return self.first.data

    def isEmpty(self):
        return self.size <= 0

class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None

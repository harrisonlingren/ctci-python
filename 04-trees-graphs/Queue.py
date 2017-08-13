class Queue(object):

    def __init__(self):
        self.first = Node(None)
        self.last = Node(None)

    def dequeue(self):
        if self.first is None:
            return None
        old = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return old

    def enqueue(self, val):
        new = Node(val)
        if self.last != None:
            self.last.next = new
        self.last = new
        if self.first is None:
            self.first = self.last

    def peek(self):
        return self.first.data

    def isEmpty(self):
        return self.first is None

class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None

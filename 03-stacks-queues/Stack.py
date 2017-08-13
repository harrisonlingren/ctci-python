class Stack(object):

    def __init__(self):
        self.top = Node(None)

    def pop(self):
        if self.top == None:
            return None
        old = self.top.data
        self.top = self.top.next
        return old

    def push(self, val):
        new = Node(val)
        new.next = self.top
        self.top = new

    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top == None

class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = Node(None)

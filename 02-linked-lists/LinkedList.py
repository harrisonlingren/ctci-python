class LinkedList(object):
    """ A simple Linked List data structure for use in this chapter"""

    def __init__(self):
        self.head = Node(None)
        self.size = 0
        self.max = 0
        self.min = 0

    def __len__(self):
        return self.size

    def __max__(self):
        return self.max

    def __min__(self):
        return self.min

    def getHead(self):
        return self.head

    def add(self, val):
        newTail = Node(val)

        # find the last node
        n = self.head
        while n.hasNext():
            n = n.getNext()

        # add to tail, increase size
        n.setNext(newTail)
        self.size += 1

        # check if min/max
        if val < self.min:
            self.min = val
        elif val > self.max:
            self.max = val

    def remove(self, val):
        # find the value
        n = self.head
        success = False
        while n.hasNext():
            if n.getNext().getVal() == val:
                success = True
                n.setNext(n.getNext().getNext())
                break
            n = n.getNext()

        # update size if successful
        if success:
            self.size -= 1
        else:
            print('could not find value %s in list' % val)

class Node(object):
    """ A simple Node structure for the LinkedList class"""

    def __init__(self, data):
        self.data = data
        self.nextN = None

    def hasNext(self):
        return True if self.nextN else False

    def getNext(self):
        if self.hasNext():
            return self.nextN

    def setNext(self, newNode):
        self.nextN = newNode

    def getVal(self):
        return self.data

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.root = Node()

class Node(object):
    def __init__(self, val=None):
        self.data = val
        self.nodes = []

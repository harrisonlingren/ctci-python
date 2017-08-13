class Graph(object):
    def __init__(self, size=1):
        self.nodes = [Node(x) for x in range(size)]

class Node(object):
    def __init__(self, val=None):
        self.data = val
        self.adjacent = []
        self.visited = False

    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)

    def addAdj(self, noderef):
        self.adjacent.append(noderef)

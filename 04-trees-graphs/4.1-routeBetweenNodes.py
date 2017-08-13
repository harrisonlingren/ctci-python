from Queue import Queue
from Graph import Graph

def routeBetweenNodes(graph, src, dest):
    # sanity check
    if src == dest:
        return True

    nodeQ = Queue()
    src.visited = True
    nodeQ.enqueue(src)

    # do BFS
    while nodeQ.isEmpty() == False:
        nextStep = nodeQ.dequeue()
        nextStep.visited = True
        for adj in nextStep.adjacent:
            if not adj.visited:
                if adj == dest:
                    return True
                adj.visited = True
                nodeQ.enqueue(adj)

    return False

# graph setup
g = Graph(9)
g.nodes[0].addAdj(g.nodes[5])
g.nodes[1].addAdj(g.nodes[0])
g.nodes[1].addAdj(g.nodes[2])
g.nodes[2].addAdj(g.nodes[5])
g.nodes[3].addAdj(g.nodes[0])
g.nodes[4].addAdj(g.nodes[3])
g.nodes[4].addAdj(g.nodes[7])
g.nodes[5].addAdj(g.nodes[4])
g.nodes[6].addAdj(g.nodes[1])
g.nodes[6].addAdj(g.nodes[3])
g.nodes[7].addAdj(g.nodes[6])
g.nodes[7].addAdj(g.nodes[8])
g.nodes[8].addAdj(g.nodes[4])

for node in g.nodes:
    print(node.data, node.visited, node.adjacent)

print('path found: %s' % routeBetweenNodes(g, g.nodes[0], g.nodes[8]))

class Graph(object):
    def __init__(self):
        self.edges = dict()

    def addVertex(self, v):
        if v not in self.edges:
            self.edges[v] = set()

    def addEdges(self, from_v, to_v):
        if from_v not in self.edges:
            self.edges[from_v] = set()

        if to_v not in self.edges:
            self.edges[to_v] = set()

        if to_v not in self.edges[from_v]:
            self.edges[from_v].add(to_v)

        if from_v not in self.edges[to_v]:
            self.edges[to_v].add(from_v)

        return True

    def isEdge(self, from_v, to_v):
        if from_v not in self.edges:
            return False

        if to_v not in self.edges:
            return False

        return to_v in self.edges[from_v]

def loadVertex(edges):
    g = Graph()
    for v in edges:
        g.addVertex(v)
        for neighbors in edges[v]:
            g.addEdges(v, neighbors)

    return g

if __name__ == '__main__':
    edges = dict(A = {'B','C'},
                 B = {'A', 'D'},
                 C = {'A' ,'E'},
                 D = {'B'},
                 E = {'C'})
    g = loadVertex(edges)
    print g.isEdge('D','F')
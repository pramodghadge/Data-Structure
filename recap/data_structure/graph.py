class Graph(object):
    def __init__(self):
        self.vertex = dict()

    def addVertex(self, v):
        if v not in self.vertex:
            self.vertex[v] = set()

    def addEdges(self, from_v, to_v):
        if from_v not in self.vertex:
            self.vertex[from_v] = set()

        if to_v not in self.vertex:
            self.vertex[to_v] = set()

        if to_v not in self.vertex[from_v]:
            self.vertex[from_v].add(to_v)

        if from_v not in self.vertex[to_v]:
            self.vertex[to_v].add(from_v)

    def isEdge(self, from_v, to_v):
        if from_v not in self.vertex:
            return False

        if to_v not in self.vertex:
            return False

        return to_v in self.vertex[from_v]

def loadVertexes(graph):
    g = Graph()
    for v in graph:
        g.addVertex(v)
        for to_v in graph[v]:
            g.addEdges(v, to_v)

    return g



if __name__ == '__main__':
    a = {
        1 : [2,3],
        2 : [4],
        3 : [5],
        4 : [6],
        5 : [6]
    }
    g = loadVertexes(a)
    print g.vertex
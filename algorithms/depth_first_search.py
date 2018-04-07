from DataStructure.graph import Graph, loadVertex

White = 0
Grey = 1
Black = 2

class DepthFirstTraversal(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.color = {}
        self.pred  = {}

        for v in graph.edges:
            self.color[v] = White
            self.pred[v] = None

        self.dfs_visit(start)

    def dfs_visit(self, start):
        self.color[start] = Grey

        for v in self.graph.edges[start]:
            if self.color[v] is White:
                self.pred[v] = start
                self.dfs_visit(v)

        self.color[start] = Black

    def solution(self,v):
        '''Recover path from start to this vertex v'''
        if v not in self.graph.edges:
            return None

        path = [v]

        if not self.pred[v]:
            return None
        while v != self.start:
            v = self.pred[v]
            path.insert(0,v)

        return path

if __name__ == '__main__':
    edges = dict(A={'B', 'C'},
                 B={'A', 'D'},
                 C={'A', 'E'},
                 D={'B'},
                 E={'C'})


    edges =  dict(
        A = {'B'},
        C = {'E'}
    )

    g = loadVertex(edges)
    dfs = DepthFirstTraversal(g, 'A')

    path = dfs.solution('B')
    print path
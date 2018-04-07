WHITE = 'W'
GREY = 'G'
BLACK = 'B'

from recap.data_structure.graph import loadVertexes

class DFS(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start

        self.color = {}
        self.pred = {}

        for v in self.graph:
            self.color[v] = WHITE
            self.pred[v] = None

        self.dfs_visits(start)

    def dfs_visits(self, start):
        self.color[start] = GREY
        for v in self.graph[start]:
            if self.color[v] == WHITE:
                self.color[v] = GREY
                self.pred[v] = start
                self.dfs_visits(v)

        self.color[start] = BLACK


    def solution(self, to_v):
        if to_v not in self.graph:
            return None

        path = [to_v]
        while to_v != self.start:
            to_v = self.pred[to_v]
            path.insert(0,to_v)
        return path

if __name__ == '__main__':
    a = {
        1 : [2,3],
        2 : [4],
        3 : [5],
        4 : [6],
        5 : [6]
    }
    g = loadVertexes(a)
    dfs = DFS(g.vertex,1)
    print dfs.solution(3)
WHITE=0
GREY=1
BLACK=2

class DFS(object):
    def __init__(self, graph, src):
        self.pred = {}
        self.color = {}
        self.graph = graph

        for v in graph:
            self.color[v] = WHITE
            self.pred[v] = None

        self.dfs_visits(src)

    def def_visits(self, src):
        self.color[src] = GREY
        for v in self.graph[src]:
            if self.color[v] != GREY:
                self.color[v] = GREY
                self.pred[v] = src
                self.def_visits(v)
        self.color[src] = BLACK

    def solution(self, a_v, b_v):
        if a_v not in self.graph:
            return False
        if b_v not in self.graph:
            return False

        a_src = self.pred[a_v]
        b_src = self.pred[b_v]

def find_common_root(toRoot, aNode, bNode):
    childrens = toRoot.childs()


    if not childrens:
        return toRoot.name
    else:
        for ch in childrens:
            name = find_common_root(ch)
            if name == aNode.name or name == bNode.name:
                return ch.name










if __name__ == '__main__':
    g = {
        'sam' : {'pete', 'katie'},
        'bob' : {'john'},
        'mary' : {'bob', 'sam'},
        'tom' : {"mary"},
        'pate' : set(),
        'katie' : set()
    }
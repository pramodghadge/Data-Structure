from recap.data_structure.graph import loadVertexes
from collections import deque

def bfs_traverse(graph, start):

    if start not in graph:
        return None
    queue = deque()
    queue.append(start)
    visited = dict()
    visited[start] = True

    newNodes = []
    newNodes.append(start)
    while queue:
        vertex = queue.pop()
        for node in graph[vertex]:
            if node in graph and node not in visited:
                visited[node] = True
                newNodes.append(node)
                queue.append(node)

    return ','.join(map(str,newNodes))

def bfs_shorted_path(graph, start, end):
    if start not in graph:
        return None

    if end not in graph:
        return None

    path = [start]
    queue = deque()
    visited = set()
    queue.append(start)
    visited.add(start)
    if start == end:
        return start

    while queue:
        vertex = queue.pop()
        for v in graph[vertex]:
            if v not in graph:
                continue
            if v not in visited:
                visited.add(v)
                path.append(v)
                if v == end:
                    print ','.join(map(str,path))
                else:
                    queue.append(v)

    return False






if __name__ == '__main__':
    a = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [6],
        5: [6]
    }
    g = loadVertexes(a)
    # print bfs_traverse(g.vertex, 1)

    bfs_shorted_path(g.vertex,1,6)

from binary_heap import BinaryHeap
import sys
def shorted_path(G, src):
    dist = {}
    pred = {}

    n = 0
    infinity = sys.maxint

    for v in G.keys():
        dist[v] = infinity
        pred[v] = None
        n +=1

    dist[src] = 0
    bh = BinaryHeap(n, src, infinity)

    while not bh.isEmpty():
        u = bh.pop()
        for v, w in G[u]:
            newLen = dist[u] + w
            if newLen < dist[v]:
                dist[v] = newLen
                bh.decreaseKey(v, newLen)
                pred[v] = u

    return dist, pred

def solution(s, v, dist, pred):
    distance = dist[v]

    path = [v]

    while v != s:
        v = pred[v]
        path.insert(0, v)

    return 'distance: {0}, path:{1}'.format(distance, str(path))

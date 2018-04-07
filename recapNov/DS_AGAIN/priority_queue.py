class Element(object):
    def __init__(self, ident, priority):
        self.ident = ident
        self.priority = priority

    def __repr__(self):
        return '[Id: '+ str(self.ident) + ', priority:'+ str(self.priority) +']'

import sys

class BinaryHeap(object):
    def __init__(self, size, src):
        self.n = size
        self.data = [None] * size
        self.order = [None] * size

        infinity = sys.maxint
        for i in range(size):
            self.data[i] = Element(i, infinity)
            self.order[i] = i

        self.order[0], self.order[src] = self.order[src] ,self.order[0]

        self.data[0] = Element(src, 0)
        self.order[src] = 0


    def add(self):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        return self.n == 0

class Element(object):
    def __init__(self, ident, priority):
        self.ident = ident
        self.priority = priority

    def __repr__(self):
        return 'Id:' + str(self.ident) + ', priority:'+ str(self.priority)

import sys
class BinaryHeap(object):
    def __init__(self, size, src, infinity=sys.maxint):
        self.n = size

        self.arr = [None] * size
        self.pos = [None] * size

        for ident in range(size):
            self.arr[ident] = Element(ident, infinity)
            self.pos[ident] = ident

        self.pos[src], self.pos[0] = self.pos[0], self.pos[src]

        self.arr[0] = Element(src, 0)
        self.pos[src] = 0


    def isEmpty(self):
        return self.n == 0

    def pop(self):
        val = self.arr[0].ident

        self.n -= 1
        last = self.arr[self.n]

        self.arr[0] = last

        pIdx = 0
        child = pIdx*2+1

        while child < self.n:
            sm = self.arr[child]
            if child < self.n:
                if sm.priority > self.arr[child+1].priority:
                    child += 1
                    sm = self.arr[child]

            if last.priority < sm.priority:
                break

            self.arr[pIdx] = sm
            self.pos[sm.ident] = pIdx

            pIdx = child
            child = pIdx*2+1

        self.arr[pIdx] = last
        self.pos[last.ident] = pIdx
        return val

    def add(self, ident, priority):
        i = self.n
        self.n +=1

        while i > 0:
            pIdx = (i-1) //2
            p = self.arr[pIdx]

            if p.priority <= priority:
                break

            self.arr[i] = p
            self.pos[p.ident] = i

            i = pIdx
        self.arr[i] = Element(ident, priority)
        self.pos[ident] = i


    def decreaseKey(self, ident, priority):
        size = self.n
        self.n = self.pos[ident]
        self.add(ident, priority)
        self.n = size


    def __repr__(self):
        """Return representation of heap as array."""
        return 'heap:[' + ','.join(map(str,self.arr[:self.n])) + '], ' + str(self.pos)

if __name__ == '__main__':
    bh = BinaryHeap(5,3)
    bh.decreaseKey(1,5)
    bh.decreaseKey(2,6)
    bh.decreaseKey(4,4)
    bh.decreaseKey(0,3)

    # print bh.pop()

    bh.decreaseKey(4,1)

    print bh














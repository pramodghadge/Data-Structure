class Element(object):
    def __init__(self, ident, priority):
        self.ident = ident
        self.priority = priority


    def __repr__(self):
        return "Ident:{0} and priority:{1}".format(str(self.ident), str(self.priority))


import sys

class BinaryHeap(object):
    def __init__(self, size, src):
        self.arr = [None] * size
        self.pos = [None] * size

        self.n = size

        for i in range(size):
            self.arr[i] = Element(i, sys.maxint)
            self.pos[i] = i


        self.pos[0], self.pos[src] = self.pos[src], self.pos[0]
        self.arr[0] = Element(src, 0)

    def heapify(self, idx):
        left = idx*2+1
        right = idx*2+2
        smallest = idx

        if left < self.n and self.arr[left].priority < self.arr[smallest].priority:
            smallest = left

        if right < self.n and self.arr[right].priority < self.arr[smallest].priority:
            smallest = right

        if idx != smallest:
            self.arr[idx] , self.arr[smallest] = self.arr[smallest], self.arr[idx]
            self.pos[idx], self.pos[smallest] = self.pos[smallest], self.pos[idx]
            self.heapify(smallest)



    def pop(self):
        element = self.arr[0]
        self.n -= 1
        self.arr[0] = self.arr[self.n]
        self.pos[self.n] = 0
        self.heapify(0)
        return element.ident
        # element = self.arr[0]
        # val = element.ident
        # self.n -= 1
        # last = self.arr[self.n]
        #
        # pIdx = 0
        # child = (pIdx *2) + 1
        #
        # while child < self.n:
        #     sm = self.arr[child]
        #     if child < self.n:
        #         if sm.priority > self.arr[child+1].priority:
        #             child += 1
        #             sm = self.arr[child]
        #     if self.arr[pIdx].priority <= sm.priority:
        #         break
        #
        #     self.arr[pIdx] = sm
        #     self.pos[child] = pIdx
        #     pIdx = child
        #     child = pIdx*2+1
        #
        # self.arr[pIdx] = last
        # self.pos[last.ident] = pIdx
        # return val


    # def add(self, ident, priority):
    #     size = len(self.arr)
    #     if self.n < size:
    #         #replace operation
    #         self.arr[self.n] = Element

    def add(self, ident, priority):
        i = self.n
        self.n += 1

        while i > 0:
            pIdx = (i-1) // 2
            p = self.arr[pIdx]
            if priority > self.arr[pIdx].priority:
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


if __name__ == '__main__':
    bh = BinaryHeap(5,3)

    bh.decreaseKey(2, 10)
    print bh.arr
    print bh.pop()
    print bh.arr
    print bh.pop()

    print bh.arr
    print bh.pop()


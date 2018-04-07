class Heap(object):
    def __init__(self, values):
        self.data = list(values)
        self.size = len(self.data)
        start = (self.size - 1) // 2
        for i in range(start, -1, -1):
            self.heapify(i)

    def heapify(self, idx):
        left = (idx * 2 ) + 1
        right = (idx * 2) + 2

        smallest = idx

        if left < self.size and self.data[left] < self.data[smallest]:
            smallest = left

        if right < self.size and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest != idx:
            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            self.heapify(smallest)

    # def pop(self):
    #     val = self.data[0]
    #     self.size -= 1
    #     self.data[0] = self.data[self.size]
    #     self.heapify(0)
    #     return val

    def pop(self):
        val = self.data[0]
        self.size -= 1
        self.data[0] = self.data[self.size]

        pIdx = 0
        child = pIdx * 2 +1

        while child < self.size:
            if child-1 < self.size and self.data[child] > self.data[child+1]:
                child += 1

            if self.data[pIdx] < self.data[child]:
                break

            self.data[pIdx], self.data[child] = self.data[child], self.data[pIdx]
            pIdx = child
            child = pIdx * 2 + 1

        return val


    def add(self, value):
        if self.size != len(self.data):
            self.data[self.size] = value
        else:
            self.data.append(value)

        i = self.size
        self.size += 1
        # start = (self.size -1 ) // 2
        # for i in range(start, -1, -1):
        #     self.heapify(i)
        while i > 0:
            pIdx = (i-1) // 2
            if self.data[pIdx] <= self.data[i]:
                break

            self.data[i], self.data[pIdx] = self.data[pIdx], self.data[i]
            i = pIdx



    def __repr__(self):
        return 'Heap:['+ str(self.data) +']'

if __name__ == '__main__':
    hp = Heap([12,34,65,8,3])
    print hp
    print hp.pop()
    print hp
    hp.add(2)
    hp.add(1)
    print hp
    print hp.pop()
    print hp.pop()
    hp.add(4)
    print hp

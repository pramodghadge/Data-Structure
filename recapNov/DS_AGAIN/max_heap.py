class Heap(object):
    def __init__(self, values):
        self.data = list(values)
        self.size = len(self.data)

        start = (self.size -1) // 2

        for i in range(start, -1, -1):
            self.heapify(i, self.size)

    def pop(self):
        val = self.data[0]

        self.size -= 1
        self.data[0] = self.data[self.size]

        pidx = 0
        child = pidx * 2 + 1
        while child < self.size:
            if child-1 < self.size and self.data[child] < self.data[child+1]:
                child += 1
            if self.data[pidx] > self.data[child]:
                break

            self.data[pidx], self.data[child] = self.data[child], self.data[pidx]
            pidx = child
            child = pidx*2+1

        return val

    def add(self, value):
        if self.size < len(self.data):
            self.data[self.size] = value
        else:
            self.data.append(value)
        i = self.size
        self.size +=1

        while i > 0:
            pidx = (i-1) // 2

            if self.data[pidx] > self.data[i]:
                break

            self.data[pidx], self.data[i] = self.data[i], self.data[pidx]
            i = pidx

    def heapify(self, idx, size):
        left = idx * 2 + 1
        right = idx * 2 + 2

        largest = idx

        if left < size and self.data[left] > self.data[largest]:
            largest = left

        if right < size and self.data[right] > self.data[largest]:
            largest = right

        if largest != idx:
            self.data[largest], self.data[idx] = self.data[idx], self.data[largest]
            self.heapify(largest, size)


    def __repr__(self):
        return 'Heap:['+','.join(map(str, self.data))+']'

    def getSorted(self):
        for i in range(self.size-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(0, size=i)
        return self.data




if __name__ == '__main__':
    hp = Heap([23,445,56,2326,3,6,10])
    print hp
    print hp.pop()
    hp.add(24)
    print hp
    print hp.getSorted()


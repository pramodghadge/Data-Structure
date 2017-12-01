class Heap(object):
    def __init__(self, values):
        self.arr = list(values)
        self.size = len(self.arr)

        parent = (self.size - 1) / 2

        for i in range(parent, -1, -1):
            self.heapify(i)

    def heapify(self, idx):
        left = (idx * 2) + 1
        right = (idx * 2) + 2
        smallest = idx
        if left < self.size and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right
        if smallest != idx:
            self.arr[smallest], self.arr[idx] = self.arr[idx], self.arr[smallest]
            self.heapify(smallest)

    def add(self, value):
        if self.size < len(self.arr):
            self.arr[0] = value
        else:
            self.arr.append(value)
        self.size += 1

        start = (self.size - 1) / 2
        for i in range(start, -1,-1):
            self.heapify(i)

    def pop(self):
        val = self.arr[0]
        self.size -= 1
        return val

    def __repr__(self):
        return 'Heap:['+','.join(map(str, self.arr))+']'

if __name__ == '__main__':
    values = [23,34,5,2,20,3,8]
    hp = Heap(values)
    print hp
    hp.add(1)
    print hp.pop()
    hp.add(0)
    print hp

class CircularBuffer(object):
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.count = 0
        self.high = 0
        self.low = 0

    def add(self, value):
        if self.isFull():
            self.low = (self.low + 1) % self.size
        else:
            self.count += 1
        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size
        return  True

    def pop(self):
        val = self.buffer[self.low]
        self.low = (self.low+1) % self.size
        return val

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.size == self.count

    def __iter__(self):
        num = self.count
        idx = self.low

        while num:
            yield self.buffer[idx]
            idx = (idx+1) % self.size
            num -= 1

    def __repr__(self):
        return 'Circular Buffer:[' + ','.join(map(str, self)) + ']'

if __name__ == '__main__':
    cb = CircularBuffer(3)
    print cb
    cb.add(4)
    cb.add(2)
    cb.add(1)
    cb.add(5)
    print cb
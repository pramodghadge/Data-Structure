class CircularBuffer(object):
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.high = 0
        self.low = 0
        self.count = 0

    def add(self,value):
        if self.isFull():
            self.low = (self.low+1) % self.size
        else:
            self.count += 1
        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size

    def pop(self):
        if self.isEmpty():
            raise ValueError('Circular Buffer is empty')
        value = self.buffer[self.low]
        self.low = (self.low+1) % self.size
        self.count -= 1
        return value

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def __iter__(self):
        idx = self.low
        num = self.count
        while num:
            yield self.buffer[idx]
            idx = (idx + 1) % self.size
            num -= 1

    def __repr__(self):
        return 'CircularBufffer:['+','.join(map(str, self))+']'

if __name__ == '__main__':
    cb = CircularBuffer(5)
    print cb
    cb.add(12)
    cb.add(13)
    cb.add(14)
    cb.add(15)
    cb.add(16)
    cb.add(17)
    print cb
    print cb.pop()
    print cb
    cb.add(18)
    print cb
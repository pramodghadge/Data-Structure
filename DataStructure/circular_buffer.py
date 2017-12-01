class CircularBuffer(object):
    def __init__(self, size=5):
        self.buffer = [None] * size
        self.size = size
        self.count = 0
        self.high = 0
        self.low  = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def add(self, value):
        if self.isFull():
            self.low = (self.low +1) % self.size
        else:
            self.count += 1
        self.buffer[self.high] = value
        self.high = (self.high+1) % self.size

    def pop(self):
        if self.isEmpty():
            raise ValueError('Buffer is empty')
        val = self.buffer[self.low]
        self.low = (self.low + 1) % self.size
        self.count -= 1
        return val

    def __iter__(self):
        idx = self.low
        num = self.count
        while num:
            yield self.buffer[idx]
            idx = (idx +1) % self.size
            num -= 1

    def __repr__(self):
        return 'CircularBuffer:['+','.join(map(str,self))+']'

if __name__ == '__main__':
    cb = CircularBuffer()
    print cb
    cb.add(2)
    print cb
    cb.add(3)
    print cb
    cb.add(4)
    print cb
    print cb.pop()
    print cb
    cb.add(2)
    print cb
    cb.add(5)
    cb.add(6)
    print cb
    cb.add(1)
    print cb
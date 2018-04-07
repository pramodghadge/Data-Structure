class CircularBuffer(object):
    def __init__(self, size=5):
        self.buffer = [None] * size
        self.size = size
        self.low = 0
        self.high = 0
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def add(self, value):
        if self.isFull():
            self.low = (self.low + 1) % self.size
        else:
            self.count += 1

        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size

    def pop(self):
        val = self.buffer[self.low]
        self.low = (self.low + 1) % self.size
        self.count -= 1
        return val

    def __iter__(self):
        idx = self.low
        num = self.count
        while num:
            yield self.buffer[idx]
            idx = (idx+1) % self.size
            num -= 1

    def __repr__(self):
        return 'CircularBuffer:[' +','.join(map(str,self))+ ']'



if __name__ == '__main__':
    cb = CircularBuffer()
    cb.add(10)
    cb.add(12)

    print cb
    print cb.pop()
    cb.add(14)
    cb.add(16)
    cb.add(18)
    print cb
    # print cb
    cb.add(20)
    print cb
    cb.add(22)
    print cb
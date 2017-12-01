from DataStructure.circular_buffer import CircularBuffer

class MovingAverage(CircularBuffer):
    def __init__(self, size=5):
        self.total = 0
        super(MovingAverage, self).__init__(size)

    def getAverage(self):
        if self.isEmpty():
            return 0
        return self.total / self.size

    def add(self, value):
        if self.isFull():
            val = - self.buffer[self.low] + value
        else:
            val = value
        self.total += val
        super(MovingAverage, self).add(value)

    def pop(self):
        if self.isEmpty():
            raise ValueError('Buffer is empty')
        self.total -= self.buffer[self.low]
        return super(MovingAverage, self).pop()

    def __repr__(self):
        return 'MovingAverage:['+','.join(map(str,self))+'], Average:['+str(self.getAverage())+']'

if __name__ == '__main__':
    ma = MovingAverage()
    print ma
    ma.add(2)
    ma.add(3)
    ma.add(2)
    ma.add(3)
    ma.add(2)
    ma.add(30)

    print ma
    print ma.pop()
    print ma


from recap.data_structure.circular_buffer import CircularBuffer

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
            a = - self.buffer[self.low] + value
        else:
            a = value
        self.total += value
        super(MovingAverage, self).add(value)

    def pop(self):
        val = self.buffer[self.low]
        self.total -= val
        return super(MovingAverage, self).pop()

    def __repr__(self):
        return 'Moving Average: ['+ ','.join(map(str,self)) +'], Average:'+ str(self.getAverage())

if __name__ == '__main__':
    ma = MovingAverage()
    print ma
    ma.add(10)
    ma.add(11)
    ma.add(12)
    print ma
    print ma.pop()
    print ma
from circular_buffer import CircularBuffer

class MovingAverage(CircularBuffer):
    def __init__(self,size):
        self.total = 0
        super(MovingAverage, self).__init__(size)

    def add(self, value):
        if self.isFull():
            k = -self.buffer[self.low] + value
        else:
            k = value
        self.total += k
        super(MovingAverage, self).add(value)

    def getAverage(self):
        if self.isEmpty():
            return 0.0
        return float(self.total) / self.size

    def __repr__(self):
        return 'MovingAverage:['+','.join(map(str,self))+'], Average: '+ str(self.getAverage())

if __name__ == '__main__':
    ma = MovingAverage(5)
    print ma
    ma.add(10)
    ma.add(20)
    ma.add(30)
    ma.add(40)
    ma.add(50)
    ma.add(60)

    print ma
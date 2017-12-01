class Queue(object):
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def pop(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        return self.data.pop(0)

    def add(self, value):
        self.data.append(value)

    def __repr__(self):
        return 'Queue:['+','.join(map(str, self.data))+']'

if __name__ == '__main__':
    q = Queue()
    q.add(10)
    q.add(11)
    q.add(12)
    print q
    print q.pop()
    print q.pop()
    print q.pop()
    print q
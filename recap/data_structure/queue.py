class Queue(object):
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop(0)

    def isEmpty(self):
        return len(self.data) == 0

    def __iter__(self):
        for i in self.data:
            yield i

    def __repr__(self):
        return 'Queue:['+','.join(map(str,self))+']'


if __name__ == '__main__':
    q = Queue()
    print q
    q.add(10)
    q.add(12)
    print q
    print q.pop()
    print q
    q.add(14)
    print q
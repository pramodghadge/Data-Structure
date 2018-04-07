class Queue(object):
    def __init__(self):
        self.data = []

    def add(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop(0)

    def isEmpty(self):
        return len(self.data) == 0

    def __iter__(self):
        queue_len = len(self.data)
        i = 0
        while queue_len > 0:
            yield self.data[i]
            i+=1
            queue_len -= 1



    def __repr__(self):
        return 'List Queue:['+','.join(map(str, self))+']'


if __name__ == '__main__':
    q = Queue()
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    print q
    print q.pop()
    print q




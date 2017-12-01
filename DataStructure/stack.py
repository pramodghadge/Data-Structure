class Stack(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def pop(self):
        return self.queue.pop()

    def add(self, value):
        self.queue.append(value)

    def __repr__(self):
        return 'Stack:['+','.join(map(str, self.queue))+']'

if __name__ == '__main__':
    st = Stack()
    st.add(10)
    st.add(11)
    st.add(12)

    print st.pop()
    st.add(13)
    print st
class Stack(object):
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            raise ValueError('Stack is empty')
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def __repr__(self):
        return 'Stack:[' + ','.join(map(str, self.data)) + ']'

if __name__ == '__main__':
    st = Stack()
    print st
    st.add(10)
    st.add(12)
    print st
    print st.pop()
    print st
    st.add(13)
    print st
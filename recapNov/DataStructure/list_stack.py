class Stack(object):
    def __init__(self):
        self.data = []

    def add(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def __iter__(self):
        for i in reversed(self.data):
            yield i
        # st_len = len(self.data)
        # while st_len != 0:
        #     st_len -= 1
        #     yield self.data[st_len]


    def __repr__(self):
        return 'List stack:['+','.join(map(str,self))+']'


if __name__ == '__main__':
    st = Stack()
    print st
    st.add(2)
    st.add(3)
    st.add(4)
    st.add(5)
    print st

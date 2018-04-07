class FindMin(object):
    def __init__(self):
        self.myStack = []
        self.myMinStack = []

    def add(self, value):
        if not self.myStack:
            self.myMinStack.append(value)
            self.myStack.append(value)
        else:
            minVal = self.getMin()
            if value < minVal:
                self.myMinStack.append(value)
            else:
                self.myMinStack.append(minVal)
        self.myStack.append(value)
    def pop(self):
        lastVal = self.myStack.pop()
        self.myMinStack.pop()
        return lastVal

    def getMin(self):
        return self.myMinStack[-1]


if __name__ == '__main__':
    stack = FindMin()
    stack.add(4)
    stack.add(5)
    stack.add(3)
    stack.add(7)
    stack.add(2)

    print stack.getMin()
    print stack.pop()
    print stack.getMin()
    print stack.pop()
    print stack.getMin()
    print stack.pop()
    print stack.getMin()
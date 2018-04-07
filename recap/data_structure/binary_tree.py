import sys
class BinaryNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            self.left = self.addToSubTree(self.left, value)
        else:
            self.right = self.addToSubTree(self.right, value)

    def addToSubTree(self, parent, value):
        if parent is None:
            parent = BinaryNode(value)
        else:
            parent.add(value)
        return parent

    def remove(self, value):
        if value < self.value:
            self.left = self.removeFromSubTree(self.left, value)
        elif value > self.value:
            self.right = self.removeFromSubTree(self.right, value)
        else:
            if self.left is None:
                return self.right

            child = self.left

            while child.right:
                child = child.right
            childValue = child.value
            self.left = self.removeFromSubTree(self.left, childValue)
            self.value = childValue

        return self

    def removeFromSubTree(self, parent, value):
        if parent:
            return parent.remove(value)
        return None

    def inOrder(self):
        if self.left:
            for v in self.left.inOrder():
                yield v

        yield self.value

        if self.right:
            for v in self.right.inOrder():
                yield v

class BinaryTree(object):
    '''Binary Tree'''
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def remove(self, target):
        if self.root:
            self.root.remove(target)


    def __contains__(self, item):
        if self.root is None:
            return False
        node = self.root
        while node:
            if item < node.value:
                node = node.left
            elif item > node.value:
                node = node.right
            elif item == node.value:
                return True

        return False

    def __iter__(self):
        node = self.root
        for i in node.inOrder():
            yield i


    def __repr__(self):
        return 'Binary Tree, InOrder:[' +','.join(map(str,self))+ ']'


def isBST(node):
    if node is None:
        return True

    return BSTUtils(node, -sys.maxint, sys.maxint)


def BSTUtils(node, minInt, maxInt):
    if node is None:
        return True

    if node.value < minInt or node.value > maxInt:
        return False

    return BSTUtils(node.left, minInt, node.value-1) & BSTUtils(node.right, node.value+1, maxInt)

def inLevelTraverse(node):

    currentLevel = [node]
    while currentLevel:
        nextlevel = []
        values = ''
        for nd in currentLevel:
            if values:
                values = '{0},{1}'.format(values, nd.value)
            else:
                values = nd.value
            if nd.left:
                nextlevel.append(nd.left)
            if nd.right:
                nextlevel.append(nd.right)
        print values
        currentLevel = nextlevel


def inLevelTraverse_withoutRec(node):
    # node.value
    leftNode = node.left
    rightNode = node.right
    while leftNode:
        print leftNode.value
        leftNode = leftNode.left
    print node.value
    while rightNode:
        print rightNode.value
        rightNode = rightNode.right



if __name__ == '__main__':
    bn = BinaryTree()
    bn.add(10)
    bn.add(8)
    bn.add(11)
    print 12 in bn
    bn.add(14)
    bn.add(16)
    bn.add(6)

    print bn

    # bn.remove(8)

    print isBST(bn.root)

    inLevelTraverse(bn.root)
    print 'traverse '
    inLevelTraverse_withoutRec(bn.root)
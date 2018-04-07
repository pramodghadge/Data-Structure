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

    def remove(self, target):
        if target < self.value:
            self.left = self.removeFromSubTree(self.left, target)
        elif target > self.value:
            self.right = self.removeFromSubTree(self.right, target)
        else:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            maxVal = child.value
            self.left = self.removeFromSubTree(self.left, maxVal)
            self.value = maxVal
        return self

    def removeFromSubTree(self, parent, value):
        if parent:
            return parent.remove(value)
        return parent

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def remove(self, target):
        if self.root is not None:
            self.root.remove(target)

    def __contains__(self, item):
        node = self.root
        while node:
            if item < node.value:
                node = node.left
            elif item > node.value:
                node = node.right
            else:
                return True
        return False


def inOrderTraversal(node):
    if node.left:
        inOrderTraversal(node.left)

    print node.value

    if node.right:
        inOrderTraversal(node.right)

def inLevelTraversal(node):
    currentLevel = [node]
    while currentLevel:
        nextLevel = []
        result = ''
        for nd in currentLevel:
            if result:
                result = '{0},{1}'.format(result, nd.value)
            else:
                result = nd.value

            if nd.left:
                nextLevel.append(nd.left)
            if nd.right:
                nextLevel.append(nd.right)
        print result
        currentLevel = nextLevel


def postOrderTraversal(node):
    if node:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print node.value

def preOrderTraversal(node):
    if node:
        print node.value
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

def isBST(node, minVal, maxVal):
    if node is None:
        return True

    if minVal > node.value or maxVal < node.value:
        return False
    return isBST(node.left, minVal, node.value-1) & isBST(node.right, node.value+1, maxVal)




if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(10)
    tree.add(12)
    tree.add(8)
    tree.add(9)
    tree.add(11)
    tree.add(14)
    tree.add(1)
    tree.add(2)

    # print 8 in tree


    inLevelTraversal(tree.root)
    print ''
    tree.remove(10)
    inOrderTraversal(tree.root)
    tree.remove(2)
    print 'in level'
    inLevelTraversal(tree.root)
    # print 'post order'
    # postOrderTraversal(tree.root)
    # print 'pre order'
    # preOrderTraversal(tree.root)
    # import sys
    # print 'is BST'
    # print isBST(tree.root, -sys.maxint, sys.maxint)
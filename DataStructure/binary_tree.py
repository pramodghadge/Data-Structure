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
            self.left =  self.removeFromSubTree(self.left, value)
        elif value > self.value:
            self.right = self.removeFromSubTree(self.right, value)
        else:
            '''find max value from left subtree and replace it'''
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
        return None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

def inOrderTraversal(tree):
    if tree is None:
        return None
    if tree.left is not None:
        inOrderTraversal(tree.left)

    print tree.value

    if tree.right is not None:
        inOrderTraversal(tree.right)

def inLevelTraversal(tree):
    if tree is None:
        return None
    root = tree.root
    currentLevel = [root]
    while currentLevel:
        value = ''
        nextLevel = []
        for node in currentLevel:
            value ='{0} {1}'.format(value, node.value)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        print value
        currentLevel = nextLevel

def isBST(node):
    if node is None:
        return True
    return BSTCheck(node, -sys.maxint, sys.maxint )

def BSTCheck(node, minInt, maxInt):
    if node is None:
        return True

    if node.value < minInt or node.value > maxInt:
        return False

    return BSTCheck(node.left, minInt, node.value-1) & BSTCheck(node.right, node.value+1, maxInt)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(10)
    tree.add(12)
    tree.add(14)
    tree.add(11)
    tree.add(8)
    tree.add(9)
    tree.add(7)

    tree.remove(12)
    inOrderTraversal(tree.root)
    print 'in level traversal'
    inLevelTraversal(tree)

    print 'BST check'

    if isBST(tree.root):
        print 'its BST'
    else:
        print 'its not BST'
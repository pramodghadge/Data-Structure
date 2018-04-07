class BinaryNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None
        self.height = 0


    def rotateLeft(self):
        newRoot = self.right
        grandSon = newRoot.left
        self.right = grandSon
        newRoot.left = self

        self.computeHeight()
        return newRoot

    def rotateRight(self):
        newRoot = self.left
        grandSon = newRoot.right
        self.left = grandSon
        newRoot.right = self

        self.computeHeight()
        return newRoot


    def rotateLeftRight(self):
        child = self.left
        newRoot = child.right
        grand1 = child.left
        grand2 = newRoot.right
        child.right = grand1
        self.left = grand2

        newRoot.left = child
        newRoot.right= self

        child.computeHeight()
        self.computeHeight()
        return newRoot

    def rotateRightLeft(self):
        pass


    def computeHeight(self):
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1

    def heightDifference(self):
        leftTarget = 0
        rightTarget = 0
        if self.left:
            leftTarget = 1 + self.left.height
        if self.right:
            rightTarget = 1 + self.right.height

        return leftTarget - rightTarget

    def add(self, value):
        newRoot = self
        if value <= self.value:
            self.left = self.addToSubTree(self.left, value)
            if self.heightDifference() == 2:
                if value <= self.left.value:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateLeft()
                    newRoot = newRoot.rotateRight()
        else:
            self.right = self.addToSubTree(self.right, value)
            if self.heightDifference() == -2:
                if value > self.right:
                    newRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRight()
                    newRoot = newRoot.rotateLeft()

        newRoot.computeHeight()
        return newRoot

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
            maxVal = child.value
            self.left = self.removeFromSubTree(self.left, maxVal)
            self.value = maxVal
        return self
    def removeFromSubTree(self, parent, value):
        if parent is not None:
            parent.remove(value)
        return parent


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self.root.add(value)


    def remove(self, target):
        if self.root:
            self.root.remove(target)

    def __contains__(self, item):
        if self.root is None:
            raise ValueError("Binary tree is empty")

        node = self.root
        while node:
            if item < node.value:
                node = node.left
            elif item > node.value:
                node = node.right
            else:
                return True
        return False


def InorderTraversal(node):
    if node is None:
        return
    InorderTraversal(node.left)
    print node.value
    InorderTraversal(node.right)



if __name__ == '__main__':
    bn = BinaryTree()
    bn.add(50)
    bn.add(30)
    bn.add(10)

    print 30 in bn

    InorderTraversal(bn.root)
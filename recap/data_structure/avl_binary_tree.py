class BinaryNode(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def rotateLeft(self):
        newRoot = self.right
        grandSon = newRoot.left
        self.right = grandSon
        newRoot.left = self

        self.computeHeight()
        return newRoot

    def rotateRight(self):
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

        return leftTarget - rightTarget # positive then

    def add(self, value):
        height = -1
        if value <= self.value:
            self.left = self.addToSubTree(self.left, value)
            if self.heightDifference() == 2:
                if value <= self.left.value:
                    newRoot = self.rotateRight()
                else:
                    newRoot = self.rotateleftRight()
        else:
            self.right = self.addToSubTree(self.right, value)
            if self.heightDifference() == -2:
                if value >= self.right.value:
                    nowRoot = self.rotateLeft()
                else:
                    newRoot = self.rotateRightLeft()

        newRoot.computeHeight()
        return newRoot

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

            newMax = child.value
            self.left = self.removeFromSubTree(self.left, newMax)
            self.value = newMax
        return self

    def removeFromSubTree(self, parent, value):
        if parent is not None:
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
        if self.root:
            self.root.remove(target)

    def __contains__(self, target):
        if self.root is None:
            return False

        node = self.root
        while node:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False


def inOrderTraversal(node):
    if node is None:
        return

    if node.left:
        inOrderTraversal(node.left)

    print node.value

    if node.right:
        inOrderTraversal(node.right)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(10)
    bt.add(12)
    bt.add(8)
    bt.add(6)
    bt.add(9)
    bt.add(11)
    bt.add(13)
    bt.remove(9)
    print 9 in bt
    inOrderTraversal(bt.root)
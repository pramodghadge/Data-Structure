import sys
from DataStructure.binary_tree import BinaryTree

def maxDepth(node):
    if node is None:
        return 0

    ldepth = maxDepth(node.left)
    rdepth = maxDepth(node.right)

    if ldepth > rdepth:
        return ldepth + 1
    else:
        return rdepth + 1

def maxDepth_1(node):
    if node is None:
        return 0

    leftDepth = maxDepth(node.left) + 1
    rightDepth = maxDepth(node.right) + 1

    return leftDepth if leftDepth > rightDepth else rightDepth


if __name__ == '__main__':

    bt = BinaryTree()
    bt.add(10)
    bt.add(8)
    bt.add(7)
    bt.add(6)
    # bt.add(4)
    # bt.add(5)
    bt.add(12)
    bt.add(11)
    bt.add(13)
    # bt.add(14)
    print maxDepth(bt.root)
    print maxDepth_1(bt.root)
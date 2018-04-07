import sys
from DataStructure.binary_tree import BinaryTree


def check_bst(node):
    return is_BST(node, -sys.maxint, sys.maxint)

def is_BST(node, minVal, maxVal):
    if node is None:
        return True

    if node.value < minVal or node.value > maxVal:
        return False

    return is_BST(node.left, minVal, node.value) and is_BST(node.right, node.value, maxVal)


if __name__ == '__main__':

    bt = BinaryTree()
    bt.add(10)
    bt.add(8)
    bt.add(7)
    bt.add(6)
    bt.add(12)
    bt.add(11)
    bt.add(13)
    print check_bst(bt.root)
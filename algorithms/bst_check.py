from recap.data_structure.binary_tree import BinaryTree

import sys
def bst(node):
    if node is None:
        return True

    return bst_check(node, -sys.maxint, sys.maxint)

def bst_check(node, minValue, maxValue):
    if node is None:
        return True

    if node.value < minValue or node.value > maxValue:
        return False

    return bst_check(node.left, minValue, node.value-1) and bst_check(node.right, node.value+1, maxValue)

def find_min(node):
    if node is None:
        return None

    if node.left is None:
        return node.value

    return find_min(node.left)

def maxDepth(node):
    if node is None:
        return 0

    # if node.left is None and node.right is None:
    #     return 0

    leftDepth = 1 + maxDepth(node.left)
    rightDepth = 1 + maxDepth(node.right)

    return leftDepth if leftDepth > rightDepth else rightDepth


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(10)
    tree.add(12)
    tree.add(14)
    tree.add(11)
    tree.add(8)
    tree.add(9)
    tree.add(7)

    if bst(tree.root):
        print 'Tree is BST'
    else:
        print 'Tree is not BST'


    print find_min(tree.root)
    print maxDepth(tree.root)
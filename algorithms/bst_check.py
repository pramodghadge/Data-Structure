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
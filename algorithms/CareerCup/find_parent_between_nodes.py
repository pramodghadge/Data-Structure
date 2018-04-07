from DataStructure.binary_tree import BinaryTree, BinaryNode

def find_node_between_nodes(node, nd1, nd2):
    if node is None:
        return None

    if nd1.value > nd2.value:
        maxVal = nd1.value
        minVal = nd2.value
    else:
        maxVal = nd2.value
        minVal = nd1.value

    while node is not None:
        if minVal <= node.value and maxVal >= node.value:
            return node.value
        elif minVal > node.value:
            node = node.right
        elif maxVal < node.value:
            node = node.left

    return None


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(10)
    bt.add(8)
    bt.add(7)
    bt.add(9)
    # bt.add(4)
    # bt.add(5)
    bt.add(12)
    bt.add(11)
    bt.add(13)

    nd1 = BinaryNode(11)
    nd2 = BinaryNode(13)

    print find_node_between_nodes(bt.root, nd1, nd2)


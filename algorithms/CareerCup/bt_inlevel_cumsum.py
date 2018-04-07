from DataStructure.binary_tree import BinaryTree

def in_level_bt_sum(node, even=True):
    currentLevel = [node]
    i = 0
    evenTotal = 0
    oddTotal = 0
    while currentLevel:
        nextLevel = []
        result = ''
        for nd in currentLevel:
            if i % 2 == 0:
                evenTotal += nd.value
            else:
                oddTotal += nd.value

            result = '{},{}'.format(result,str(nd.value))
            if nd.left is not None:
                nextLevel.append(nd.left)

            if nd.right is not None:
                nextLevel.append(nd.right)
        print result
        i += 1
        currentLevel = nextLevel

    if even:
        return evenTotal
    return oddTotal

if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(10)
    bt.add(8)
    bt.add(6)
    bt.add(9)
    bt.add(12)
    bt.add(11)
    bt.add(13)

    print in_level_bt_sum(bt.root, even=False)
    # 10
    # 8 12
    # 6 9 11 13
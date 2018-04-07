
 # A node
class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

import sys
# from pprint import pprint



def get_cheapestCost(rootNode):
    childs = rootNode.children

    if not childs:
        return rootNode.cost
    else:
        mincost = sys.maxint
        for child in childs:
            tempCost = get_cheapestCost(child)
            if tempCost < mincost:
                mincost = tempCost

        return mincost + rootNode.cost

if __name__ == '__main__':
    node1 = Node(1)
    node1_1 = Node(1)

    node1_1.children.append(node1)
    node2 = Node(2)
    node2.children.append(node1_1)

    node3 = Node(3)
    node3.children.append(node2)

    rootNode = Node(0)

    node4 = Node(4)
    node5 = Node(5)
    node5.children.append(node4)

    node10 = Node(10)
    node0 = Node(0)
    node0.children.append(node10)

    node3.children.append(node0)

    node1 = Node(1)
    node5_1 = Node(5)
    node6 = Node(6)
    node6.children.append(node1)
    node6.children.append(node5_1)

    rootNode.children.append(node5)
    rootNode.children.append(node3)
    rootNode.children.append(node6)

    # print pprint(rootNode)
    minCost = get_cheapestCost(rootNode)
    print minCost
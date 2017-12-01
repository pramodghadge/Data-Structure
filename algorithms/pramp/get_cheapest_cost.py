import sys
def get_cheapest_cost(rootNode):
    if not rootNode:
        return

    childrens = rootNode.children

    if not childrens:
        return rootNode.cost

    else:
        minCost = sys.maxint
        for node in childrens:
            cost = get_cheapest_cost(node)
            if cost < minCost:
                minCost = cost

        return minCost + rootNode.cost





##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

    # def addChild(self,node):
    #     node.parent=self
    #     self.children.append(node)
    #
    # def __repr__(self):
    #     return str(self.cost)

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
    minCost = get_cheapest_cost(rootNode)
    print minCost








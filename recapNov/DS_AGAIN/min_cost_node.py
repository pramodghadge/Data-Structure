import sys
def getShortestDistance(rootNode):
    childs = rootNode.childs()
    if not childs:
        return rootNode.cost
    else:
        minCost = sys.maxint
        for child in childs:
            cost = getShortestDistance(child)
            if cost < minCost:
                minCost = cost

        return rootNode.cost + minCost

def max_depth(node):
    if node is None:
        return 0

    leftMax = max_depth(node.left) + 1
    rightMax = max_depth(node.right) + 1

    return leftMax if leftMax > rightMax else rightMax
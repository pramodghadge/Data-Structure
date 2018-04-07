def get_max_profit(aList):
    minVal = aList[0]
    maxProfit = 0

    for i in range(1, len(aList)):
        if aList[i] < minVal:
            minVal = aList[i]
        else:
            diff = aList[i] - minVal
            if maxProfit < diff:
                maxProfit = diff

    return maxProfit


if __name__ == '__main__':
    aList = [3,6,2,6,9]
    print get_max_profit(aList=aList)

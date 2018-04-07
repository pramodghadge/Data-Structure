def maxProfit(aList):
    minVal = aList[0]
    profit = 0

    sellProfit = 0
    maxVal = aList[0]

    for i in range(1, len(aList)):
        if aList[i] < minVal:
            minVal = aList[i]
        else:
            if profit < (aList[i] - minVal):
                profit = aList[i] - minVal

        if aList[i] > maxVal:
            maxVal = aList
        else:
            if sellProfit < (maxVal - aList[i]):
                sellProfit = maxVal - aList[i]

    return profit if profit > sellProfit else sellProfit



if __name__ == '__main__':
    aList = [11,4,2,6,7,10,9,8,1]
    print maxProfit(aList)
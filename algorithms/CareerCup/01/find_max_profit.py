def get_max_profit(aList):
    minVal = aList[0]
    maxProfit = 0

    for i in range(1, len(aList)):
        if aList[i] < minVal:
            minVal = aList[i]
        else:
            profit = aList[i] - minVal
            if profit > maxProfit:
                maxProfit = profit

    return maxProfit


if __name__ == '__main__':
    aList = [2,20,3,40,3,1,50]
    print get_max_profit(aList)

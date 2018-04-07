def find_min_or_sum(aList):
    aMin = 1
    aSum = 0
    isAllNegative = True

    for i in aList:
        aSum += i
        if i > 0:
            isAllNegative = False
        elif i < aMin:
            aMin = i

    if isAllNegative:
        return aMin
    return aSum

if __name__ == '__main__':
    aList = [-2,-3,-4,-5,-8,-7,-9]
    print find_min_or_sum(aList)
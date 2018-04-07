def find_sum(aList, target):
    sum = 0
    tail = 0

    for i in aList:
        sum += i
        while sum > target:
            sum -= aList[tail]
            tail += 1

        if sum == target:
            return True

    return False


def findSum(aList, sumVal):
    idx = 1
    temp = aList[0]

    while idx < len(aList):
        while idx < len(aList) and (temp + aList[idx]) <= sumVal :
            temp += aList[idx]
            idx += 1

        if temp == sumVal:
            return True

        idx += 1

    return False


if __name__ == '__main__':
    aList = [6,5,3,2,1,7]
    print find_sum(aList, 15)
    print findSum(aList,15)
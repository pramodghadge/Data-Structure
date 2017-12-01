def binarySearch(aList, target):
    high = len(aList)-1
    low = 0

    while low <= high:
        mid = (low+high) / 2
        if target < aList[mid]:
            high = mid - 1
        elif target > aList[mid]:
            low = mid + 1
        else:
            return True
    return False

if __name__ == '__main__':
    aList = [2,4,6,8,10,12,14,16,18]
    print binarySearch(aList, 0)
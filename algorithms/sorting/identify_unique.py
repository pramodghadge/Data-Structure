def find_unique(aList):
    idx = 0
    size = len(aList)

    while idx < size:
        if idx < size-1 and aList[idx] == aList[idx+1]:
            idx += 2
        elif idx == 0:
            return idx
        elif idx > 0 and aList[idx-1] != aList[idx]:
            return idx
        else:
            idx += 1

    return False

def findNMakeUnique(aList):
    # [1, 1, 3, 3, 4, 5, 5, 5, 5, 6, 7, 7, 7, 8]
    size = len(aList)
    j = size -1
    for i in range(size-1, 0, -1):
        if aList[i] == aList[i-1]:
            # aList[i] = 0
            j -= 1
        else:
            aList[j] = aList[i]

    print j
    print aList


if  __name__ == '__main__':
    aList = [3, 3,4, 5, 5, 6, 7, 7, 7]
    print find_unique(aList)
    # print findNMakeUnique(aList)
    print aList



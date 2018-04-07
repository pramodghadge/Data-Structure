def moving_zero(aList):
    idx = 0
    high = len(aList)-1

    while idx < high:
        if aList[idx] == 0:
            while aList[high] == 0:
                high -= 1
            aList[idx], aList[high] = aList[high], aList[idx]
            high-=1
        idx += 1

    print aList
if __name__ == '__main__':
    a = [1,2,3,0,4,5,0,6,7,8]

    moving_zero(a)
    print a
def moving_zero(aList):
    idx = 0
    size = len(aList)
    high = size -1

    while idx < high:
        if aList[idx] == 0:
            while aList[high] == 0:
                high -= 1
            aList[idx] = aList[high]
            aList[high] = 0
            high -= 1
        idx +=1


def moving_zero_inorder(aList):
    pos = 0
    idx = 0
    size = len(aList)
    while idx < size:
        if aList[idx] != 0:
            aList[pos] = aList[idx]
            pos += 1
        idx += 1

    for i in range(pos, size):
        aList[i] = 0





if __name__ == '__main__':
    aList = [1,3,0,2,4,0,3,5,6,0,5]
    # moving_zero(aList)
    print moving_zero_inorder(aList)
    print aList

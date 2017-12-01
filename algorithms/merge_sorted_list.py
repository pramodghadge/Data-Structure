def merge(aList, bList):
    i = j = 0
    b = []
    totalLen = len(aList) + len(bList)

    while len(b) < totalLen:
        if j >= len(bList) or (i < len(aList) and aList[i] < bList[j]):
            b.append(aList[i])
            i+= 1
        elif j < len(bList):
            b.append(bList[j])
            j+=1
    return b

if __name__ == '__main__':
    aList = [2,3,4,6,8,12]
    bList = [1,5,7,9,10,11]

    print merge(aList, bList)
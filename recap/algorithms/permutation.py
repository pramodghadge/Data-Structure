def permute(aList, left, right):
    if left == right:
        print ''.join(aList)

    else:
        for i in range(left, right+1):
            aList[left], aList[i] = aList[i], aList[left]
            permute(aList, left+1, right)
            aList[left], aList[i] = aList[i], aList[left]


if __name__ == '__main__':
    myStr = 'ABCD'
    myList = list(myStr)
    permute(myList, 0, len(myList)-1)
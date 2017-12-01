def permute(aList, left, right):
    if left == right:
        print ''.join(aList)
    else:
        for i in range(left, right+1):
            aList[i], aList[left] = aList[left], aList[i]
            permute(aList, left+1, right)
            aList[i], aList[left] = aList[left], aList[i]


if __name__ == '__main__':
    myStr = 'ABC'
    aList = list(myStr)
    permute(aList=aList, left=0, right=len(aList)-1)
def find_window(aList, diff):
    counterPart = set()
    results = []
    for i in aList:
        positiveCp = diff + i
        negativeCp = i - diff
        if positiveCp in counterPart:
            print 'positive'+ str(positiveCp)
            results.append((positiveCp, i))

        if negativeCp in counterPart:
            print 'negative' + str(negativeCp)
            results.append((i, negativeCp))

        # print i, positiveCp, negativeCp
        counterPart.add(i)
        # print counterPart
    return results


def window_check(aList, k):
    mySet = set()
    results= []
    for i in aList:

        if not mySet:
            mySet.add(i)
            continue
        uBound = i + k
        lBound = i - k

        if uBound in mySet:
            results.append((uBound,i))
        if lBound in mySet:
            results.append((i,lBound))
        mySet.add(i)
    return results


if __name__ == '__main__':
    aList=[0,4,2,1,3, -2]
    print aList
    print find_window(aList, 2)
    print window_check(aList, 2)
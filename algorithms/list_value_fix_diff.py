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


if __name__ == '__main__':
    aList=[0,4,2,1,3]
    print aList
    print find_window(aList, 2)
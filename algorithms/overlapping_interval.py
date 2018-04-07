
def interate(aList):
    sortedList = sorted(aList, key=lambda x: x[0])

    maxLen = len(sortedList)-1
    i = 0
    while i <= maxLen:
        if i+1 <= maxLen and sortedList[i+1][0] < sortedList[i][1]:
            yield sortedList[i][0], sortedList[i+1][1]
        i+=2



def check_overlap(myList):
    size = len(myList) - 1
    num = 0
    results = []
    while num < size:
        a = myList[num]
        b = myList[num+1]
        if b[0] < a[1]:
            results.append((a[0], b[1]))
        num += 1
    return results
if __name__ == '__main__':
    myList = [(1, 3), (2, 4), (5, 7), (6, 8), (10,12), (13, 15), (16,18), (17,19), (20,21)]
    for i in interate(myList):
        print i
    print check_overlap(myList)


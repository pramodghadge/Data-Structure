
def interate(aList):
    sortedList = sorted(aList, key=lambda x: x[0])

    maxLen = len(sortedList)-1
    i = 0
    while i <= maxLen:
        if i+1 <= maxLen and sortedList[i+1][0] < sortedList[i][1]:
            yield sortedList[i][0], sortedList[i+1][1]
        i+=2


if __name__ == '__main__':
    myList = [(1, 3), (2, 4), (5, 7), (6, 8), (10,12), (13, 15), (16,18), (17,19), (20,21)]
    for i in interate(myList):
        print i



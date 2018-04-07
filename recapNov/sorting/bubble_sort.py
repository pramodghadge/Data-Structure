def bubble_sort(aList):
    for i in range(len(aList)):
        for j in range(len(aList)-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]


def bubble_sort_1(aList):
    for i in range(len(aList)-1,0,-1):
        for j in range(i):
            if aList[j] > aList[j+1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]

if __name__ == '__main__':
    aList = [2,45,6,1,9,7,0]
    # bubble_sort(aList)
    # print aList
    bubble_sort_1(aList)
    print aList
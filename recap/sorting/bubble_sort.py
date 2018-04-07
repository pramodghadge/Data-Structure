def bubble_sort(aList):
    for i in range(len(aList)-1, 0, -1):
        for j in range(i):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]


if __name__ == '__main__':
    aList = [23,3,5,34,65,20,10]
    bubble_sort(aList)
    print aList
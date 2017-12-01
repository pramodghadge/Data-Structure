def bubble_sort(aList):
    for i in range(len(aList)-1, 0, -1):
        for j in range(i):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]



if __name__ == '__main__':
    aList = [2,4,0,23,5,20,17,16]
    bubble_sort(aList)
    print aList
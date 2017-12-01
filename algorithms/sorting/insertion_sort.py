def insertion_sort(aList):
    for i in range(1,len(aList)):
        insert(aList, i, aList[i])

def insert(aList, idx, value):
    idx -= 1
    while idx >= 0 and aList[idx] > value:
        aList[idx+1] = aList[idx]
        idx -= 1

    aList[idx+1] = value

if __name__ == '__main__':
    aList = [2, 4, 0, 23, 5, 20, 17, 16]
    insertion_sort(aList)
    print aList
from DataStructure.max_heap import buildHeap, heapify

def heapSort(aList):
    buildHeap(aList)

    for i in range(len(aList)-1, 0, -1):
        aList[0], aList[i] = aList[i], aList[0]
        heapify(aList,0, i)

if __name__ == '__main__':
    values = [23,34,5,2,20,3,8]
    heapSort(values)
    print values
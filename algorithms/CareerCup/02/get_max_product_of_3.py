def heapify(aList, idx, size):
    left = idx*2+1
    right = idx*2+2

    largest = idx

    if left < size and aList[left] > aList[largest]:
        largest = left

    if right < size and aList[right] > aList[largest]:
        largest = right

    if idx != largest:
        aList[idx], aList[largest] = aList[largest], aList[idx]
        heapify(aList,largest,size)

def buildHeap(aList):
    size = len(aList)
    start = (size -1) // 2

    for i in range(start, -1, -1):
        heapify(aList, i, size)

def get_max_product(aList,k):
    buildHeap(aList)
    size = len(aList)
    out = 1
    for i in range(size-1,size-k-1 ,-1):
        out *= aList[0]
        aList[0], aList[i] = aList[i], aList[0]
        heapify(aList, 0, i)

    return out

if __name__ == '__main__':
    aList=range(5)
    print get_max_product(aList, k=3)
def heap_sort(aList):
    build_heap(aList)

    for i in range(len(aList)-1, 0, -1):
        aList[i], aList[0] = aList[0], aList[i]
        heapify(aList, 0 , i)


def build_heap(aList):
    size = len(aList)

    start = (size -1 ) / 2

    for i in range(start, -1, -1):
        heapify(aList, i, size)


def heapify(aList, idx, maxSize):
    left = (idx * 2) + 1
    right = (idx * 2 ) + 2

    largest = idx

    if left < maxSize and aList[left] > aList[largest]:
        largest = left

    if right < maxSize and aList[right] > aList[largest]:
        largest = right

    if largest != idx:
        aList[idx], aList[largest] = aList[largest], aList[idx]
        heapify(aList, largest, maxSize)


if __name__ == '__main__':
    aList = [23,3,5,34,65,20,10]
    heap_sort(aList)
    print aList
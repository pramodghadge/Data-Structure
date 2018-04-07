def buildHeap(aList):
    maxLen = len(aList)
    start = (maxLen -1 ) /2
    for i in range(start, -1, -1):
        heapify(aList, i, maxLen)


def heapify(aList, idx, maxLen):
    left = (idx * 2) + 1
    right = (idx * 2) + 2

    largest = idx
    if left < maxLen and aList[left] > aList[largest]:
        largest = left
    if right < maxLen and aList[right] > aList[largest]:
        largest = right

    if largest != idx:
        aList[largest], aList[idx] = aList[idx], aList[largest]
        heapify(aList, largest, maxLen)


def nth_smallest(aList, n):

    collection  = aList[:n]
    buildHeap(collection)
    for i in range(n, len(aList)):
        if aList[i] < collection[0]:
            collection[0] = aList[i]
            heapify(collection, 0, n)

    return collection[0]

if __name__ == '__main__':
    myList = range(1,100)
    print nth_smallest(myList, 6)
def buildHeap(aList):
    max = len(aList)
    parent = (max -1 ) / 2
    for i in range(parent, -1, -1):
        heapify(aList, i, max)

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


if __name__ == '__main__':
    values = [23,34,5,2,20,3,8]
    buildHeap(values)
    print values
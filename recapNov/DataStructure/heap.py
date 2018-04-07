def buildHeap(aList):
    size = len(aList)
    start = (size-1) / 2
    for i in range(start, -1, -1):
        heapify(aList, i, size)

def heapify(aList, idx, size):
    left = (idx * 2) + 1
    right = (idx * 2) + 2

    smallest = idx
    # print size, idx
    if left < size and aList[left] < aList[smallest]:
        smallest = left

    if right < size and aList[right] < aList[smallest]:
        smallest = right

    if smallest != idx:
        aList[idx], aList[smallest] = aList[smallest], aList[idx]
        heapify(aList,smallest, size)

def getKLargest(aList, k):
    subSeq = aList[:k]
    buildHeap(subSeq)
    for i in range(k, len(aList)):
        if aList[k] > subSeq[0]:
            subSeq[0] = aList[k]
            heapify(subSeq ,0, k)

    return subSeq[0]


if __name__ == '__main__':
    aList = [23,4,45,6,73,2,34]
    # buildHeap(aList)
    print aList
    print getKLargest(aList, 2)

def buildHeap(aList):
    maxLen = len(aList)

    start = (maxLen - 1 ) / 2
    for i in range(start, -1, -1):
        heapify(aList, i, maxLen)

def heapify(aList, idx, maxLen):
    left = (idx * 2) + 1
    right = (idx * 2) + 2

    smallest = idx
    if left < maxLen and aList[left] < aList[smallest]:
        smallest = left

    if right < maxLen and aList[right] < aList[smallest]:
        smallest = right

    if smallest != idx:
        aList[smallest], aList[idx] = aList[idx], aList[smallest]
        heapify(aList, smallest, maxLen)


def nth_largest(aList, n):
    collections = aList[:n]

    buildHeap(collections)

    for i in range(n, len(aList)):
        if aList[i] > collections[0]:
            collections[0] = aList[i]
            heapify(collections, 0, n)

    return collections[0]


if __name__ == '__main__':
    aList = range(1,100)
    print nth_largest(aList, 5)
def buildHeap(aList):
    maxLen = len(aList)
    start = (maxLen -1 ) / 2

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
        aList[idx],aList[smallest] = aList[smallest], aList[idx]
        heapify(aList, smallest, maxLen)

def kthLargest(aList, k):
    A = aList[:k]
    buildHeap(A)

    for i in range(k, len(aList)):
        if aList[i] > A[0]:
            A[0] = aList[i]
            heapify(A, 0, k)
    return A[0]

if __name__ == '__main__':
    values = range(100)
    print kthLargest(values,2)

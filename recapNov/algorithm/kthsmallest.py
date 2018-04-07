def buildHeap(aList):
    size = len(aList)
    start = (size - 1) / 2
    for i in range(start, -1, -1):
        heapify(aList, i, size)


def heapify(aList, idx, size):
    left = (idx * 2) + 1
    right = (idx * 2) + 2

    largest = idx

    if left < size and aList[left] > aList[largest]:
        largest = left

    if right < size and aList[right] > aList[largest]:
        largest = right

    if idx != largest:
        aList[idx], aList[largest] = aList[largest], aList[idx]
        heapify(aList, largest, size)

def kthsmallest(aList, k):
    part = aList[:k]
    buildHeap(part)

    for i in range(k, len(aList)):
        if aList[i] < part[0]:
            part[0] = aList[i]
            heapify(part, 0, k)

    return part[0]



def heapSort(aList):
    buildHeap(aList)

    for i in range(len(aList)-1,0, -1):
        aList[0], aList[i] = aList[i], aList[0]
        heapify(aList, 0, i)

if __name__ == '__main__':
    aList = [23,4,45,6,73,2,34]
    # buildHeap(aList)
    # print aList
    # 2,4 6
    print kthsmallest(aList,4)
    heapSort(aList)
    print aList
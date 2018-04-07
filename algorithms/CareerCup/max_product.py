def max_product(aList, k):
    buildHeap(aList)

    size = len(aList)-1

    maxProduct = 1
    for idx in range(size, size-k, -1):
        print aList[0]
        maxProduct *= aList[0]
        aList[0], aList[idx] = aList[idx], aList[0]
        heapify(aList, 0, idx)

    return maxProduct

def buildHeap(aList):
    size = len(aList)
    start = size -1 / 2

    for i in range(start, -1, -1):
        heapify(aList,i, size)


def heapify(aList, idx, size):
    left = (idx*2) + 1
    right = (idx*2) + 2

    largest = idx

    if left < size and aList[largest] < aList[left]:
        largest = left

    if right < size and aList[largest] < aList[right]:
        largest = right

    if idx != largest:
        aList[idx], aList[largest] = aList[largest], aList[idx]
        heapify(aList, largest, size)


if __name__ == '__main__':
    aList = [1,2,5,7,4,9,8]
    print max_product(aList, 3)

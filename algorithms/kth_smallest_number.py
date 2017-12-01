
from DataStructure.max_heap import buildHeap, heapify

def kthSmallest(aList, k):
    subList = aList[:k]
    buildHeap(subList)

    for i in range(k, len(aList)):
        if aList[i] < subList[0]:
            subList[0] = aList[i]
            heapify(subList, 0 , k)
    return subList[0]

if __name__ == '__main__':
    values = [23, 34, 5, 2, 20, 3, 8]
    k = kthSmallest(values, 5)
    print k

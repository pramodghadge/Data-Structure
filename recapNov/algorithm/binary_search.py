def binary_search(aList, target):
    low = 0
    high = len(aList) - 1

    while low <= high:
        mid = (low +high) / 2

        if target < aList[mid]:
            high = mid-1
        elif target > aList[mid]:
            low = mid +1
        else:
            return True

    return False

if __name__ == '__main__':
    aList = [ 12, 23, 34, 45, 56, 60]
    print binary_search(aList, 13)
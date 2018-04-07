def shift_list(aList,k):
    low = k-1
    size = len(aList)
    num = size

    while num > 0:
        print aList[low]
        low = (low + 1) % size
        num -= 1


if __name__ == '__main__':
    aList = range(20)
    shift_list(aList, 4)
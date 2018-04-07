def print_overLap_interval(aList):
    idx = 0
    tail = 0
    size = len(aList)

    result = []
    while idx < size:
        lower, higher = aList[idx]
        while tail < size-1 and higher > aList[tail+1][1]:
            tail += 1
        if idx != tail:
            result.append((aList[idx][0], aList[tail][1]))
            tail += 1
            idx = tail
        else:
            idx += 1
            tail += 1
    return result


if __name__ == '__main__':
    myList = [(1, 7), (2, 4), (5, 6), (6, 8), (10, 16), (13, 15), (16, 22), (17, 19), (20, 21)]
    print print_overLap_interval(myList)

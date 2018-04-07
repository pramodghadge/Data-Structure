
def find_min_common(aList, bList, cList):
    i =j =k =0

    while i < len(aList) and j < len(bList) and k < len(cList):
        if aList[i] == bList[j] == cList[k]:
            return aList[i]
        elif aList[i] < bList[j]:
            i += 1
        elif bList[j] < cList[k]:
            j += 1
        else:
            k += 1


if __name__ == '__main__':
    a = [2,3,5,6,7,8]
    b = [4,5,6,7,8]
    c = [7,8,9,10]

    print find_min_common(a,b,c)
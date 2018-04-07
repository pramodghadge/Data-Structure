def find_first_unique(aList):
    tail = 0
    j = 1
    size = len(aList)

    while j < size:
        if aList[tail] != aList[j]:
            return tail
        else:
            tail += 1
            aList[tail] = aList[j]
        j+=1




if __name__ == '__main__':
    print find_first_unique([1,1,3,4,5,5,6,7,7])


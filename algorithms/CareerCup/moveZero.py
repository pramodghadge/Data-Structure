'''
* Given an unsorted integer array, place all zeros to the end of the array without changing the sequence of non-zero
* elements. (i.e. [1,3,0,8,12, 0, 4, 0,7] --> [1,3,8,12,4,7,0,0,0])

'''
def move_zero(myList):
    pos=0
    for i,v in enumerate(myList):
        if v != 0:
            myList[pos] = myList[i]
            pos += 1

    for i in range(pos, len(myList)):
        myList[i] =0

if __name__ == '__main__':
    myList = [1,2,3,0,4,5,0,6,7,8]
    move_zero(myList)
    print myList

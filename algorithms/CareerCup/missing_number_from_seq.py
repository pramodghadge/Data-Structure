'''
Given an array A [0, 1, 3, 4,9,5,7,6] and number N.
This means that the array consists of the numbers
from 0 ... N. However, as you see, 8 is missing in A. Print the missing number.

'''

def find_missing(aList):
    ''' N(N+1)/2'''
    size = len(aList)
    totalSum = size * (size+1) / 2
    return totalSum - sum(aList)


if __name__ == '__main__':
    aList=[0,1,2,3,4,5,6,7,9]
    print find_missing(aList)


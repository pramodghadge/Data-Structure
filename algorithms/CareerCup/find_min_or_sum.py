'''
You are given an array of integers both negative and positive.
Print the maximum continuous sum of the array and if all the elements are negative,
 print the smallest of them.
Ex : [-20, -5, -2, -9] :> -2(-2)
Ex : [20, -19, 6, 9, 4] :-> 20(20)
Ex : [10, -3, 4, -2, -1, 10] -> 18 (10, -3, 4, -2, -1, 10)

'''
import sys
def find_min_or_sum(myList):
    isALlNe = True
    minNum = sys.maxint
    total = 0
    for i in myList:
        total += i
        if i < 0:
            if i < minNum:
                minNum = i
        else:
            isALlNe = False

    if not isALlNe:
        return total
    return minNum


if __name__ == '__main__':
    print find_min_or_sum([-20, -5, -2, -9])
    print find_min_or_sum([20, -19, 6, 9, 4])
    print find_min_or_sum([10, -3, 4, -2, -1, 10])
'''
One question containing multiple questions
1) Define the structure of a function which takes an array of size n as input and returns True or False.
2) Write a function which takes an array as input and returns a string containing all the elements separated by a comma.
Ex : [0, -45, 9, 10] => "0,-45,9,10";
3) Write a function which takes two arrays ass input, and returns minimum common element in them.
Ex : [0, -90, 45, 10, 4], [4, 8, 90, 45] => 4
4) Now let's say, the function takes an array of arrays, and each array is sorted. now, returns their first common element.
Ex : [0, -90, 45, 10, 4], [4, 8, 90, 45], [-1, -3, -5, -7, 10, 4], [24, 35, 78, -90, 56, 4] => 4

'''


import sys
def minimumCommon(myList1, myList2):
    mySet = set(myList1)
    minVal =  sys.maxint
    for i in myList2:
        if i in mySet:
            if i < minVal:
                minVal = i

    return minVal

def find_common(arr1, arr2, arr3):
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)

    i =j =k = 0
    while(i< n1 and j< n2 and k < n3):
        if arr1[i] == arr2[j] == arr3[k]:
            return arr1[i]
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1



if __name__ == '__main__':
    myList1 = [1,2,3,4]
    myList2 = [0, 4, 8, 45, 90]
    myList3 = [0, 1, 2, 3, 4]
    print find_common(myList1, myList2, myList3)
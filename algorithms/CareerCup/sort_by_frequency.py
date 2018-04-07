'''
Sort elements by frequency,
print the elements of an array in the decreasing frequency if 2 numbers
have same frequency then print the one which came first.
'''

def sortByFreq(myList):
    mydict = {}
    for i in myList:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1

    # print mydict
    # print mydict.items()
    for k,v in sorted(mydict.items(), key=lambda x: x[1], reverse=True):
        print k,v



if __name__ == '__main__':
    myList = [4,5,2,6,3,5,3,4,1,10,3,5,8,7,6,9,2,5,5,3,3,4]
    sortByFreq(myList)



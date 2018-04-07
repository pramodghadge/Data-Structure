'''
Given a list of URLs entered by a user write a program to
print unique and most recently used URLs. For example if user entered the following: -
1. google.com
2. yahoo.com
3. wsj.com
4. google.com

The output should be :-
1. google.com
2. wsj.com
3.yahoo.com

'''

from collections import OrderedDict

def recentOrder(myList):
    myDict = OrderedDict()
    for i in myList:
        if i not in myDict:
            myDict[i] = 1
        else:
            del myDict[i]
            myDict[i] = 1
    for i in reversed(myDict):
        print i


if __name__ == '__main__':
    recentOrder(['google.com','yahoo.com','wsj.com','google.com'])
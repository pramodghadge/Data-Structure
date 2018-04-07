def get_distinct_pattern(aList):
    myDict = {}
    for val in aList:
        newVal = ''.join(set(val))
        if newVal in myDict:
            myDict[newVal] += 1
        else:
            myDict[newVal] = 1

    for k, v in myDict.items():
        print '{0}:{1}'.format(k, str(v))


if __name__ == '__main__':
    aList = ['abba','ab', 'ba','abcd','abdc', 'adbc','aabddc']
    get_distinct_pattern(aList)
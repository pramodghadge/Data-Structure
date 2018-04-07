def getValue(myStr):
    if myStr == 'I':
        return 1
    elif myStr == 'V':
        return 5
    elif myStr == 'X':
        return 10
    elif myStr == 'L':
        return 50
    elif myStr == 'C':
        return 100
    elif myStr == 'D':
        return 500
    elif myStr == 'M':
        return 1000
    else:
        return -1

def romanToNumber(myRoman):
    size = len(myRoman)
    i = 0

    result = 0
    while i < size:
        val = getValue(myRoman[i])
        if i+1 < size:
            nextVal = getValue(myRoman[i+1])
            if val >= nextVal:
                result += val
                i += 1
            else:
                result += (nextVal - val)
                i = i + 2
        else:
            result += val
            i += 1
    return result

def sort_string(myStr):
    myList = [tuple(i.strip().split(' ')) for i in myStr.split(',')]
    # print myList
    mynewList = []
    for i in myList:
        mynewList.append((i[0], romanToNumber(i[1]), i[1]))
    print mynewList

    myResult = []
    for tup in sorted(mynewList, key=lambda x: (x[0],x[1])):
        myResult.append('{0} {1}'.format(tup[0],tup[2]))

    return ','.join(myResult)

if __name__ == '__main__':
    print romanToNumber('VIII')
    # print romanToDecimal_bak('XI')
    print sort_string('Henry II, Edward VIII')
    print sort_string('Richard V, Richard II, Richard X')
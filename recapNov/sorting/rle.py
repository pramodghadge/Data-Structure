def rle(myStr):
    result = None
    last = myStr[0]
    count = 1
    maxLen = len(myStr)
    i = 1
    while i <= maxLen:
        if i < maxLen and last == myStr[i]:
            count +=1
        else:
            if result:
                result = '{0}{1}{2}'.format(result, last, count)
            else:
                result = '{0}{1}'.format(last, count)
            count = 1
        if i < maxLen:
            last = myStr[i]
        i += 1
    return result

if __name__ == '__main__':
    print rle('abcdaeee')
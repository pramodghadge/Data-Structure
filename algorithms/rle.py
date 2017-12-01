def rle(myStr):
    result = ''
    i = 0
    maxSize = len(myStr)-1
    count = 1
    result = ''
    while i <= maxSize:
        if i != maxSize and myStr[i] == myStr[i+1]:
            count += 1
        else:
            if result:
                result = '{0}{1}{2}'.format(result,myStr[i], count)
            else:
                result = '{0}{1}'.format(myStr[i], count)
            count = 1
        i+=1
    return result


if __name__ == '__main__':
    print rle('aabcdef')
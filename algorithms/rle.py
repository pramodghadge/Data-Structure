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


def rle_again(myStr):
    size = len(myStr)
    last = myStr[0]
    count = 1
    result = None
    for idx in range(1, size+1):
        if idx == size:
            result = '{0}{1}{2}'.format(result, last, count)
            continue
        if myStr[idx] == last:
            count += 1
        else:
            if not result:
                result = '{0}{1}'.format(last,count)
            else:
                result = '{0}{1}{2}'.format(result, last, count)
            last = myStr[idx]
            count = 1
    return result

if __name__ == '__main__':
    print rle('aabcdef')
    print rle_again('aabcdedff')
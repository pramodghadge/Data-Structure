def rle(myStr):
    result = []
    idx = 1
    last = myStr[0]
    size = len(myStr)
    count = 1
    while idx <= size:
        if idx < size and last == myStr[idx]:
            count +=1
        else:
            result.extend((last,str(count)))
            count = 1
        if idx < size:
            last = myStr[idx]
        idx += 1

    return ''.join(result)

if __name__ == '__main__':
    print rle('aabccf')
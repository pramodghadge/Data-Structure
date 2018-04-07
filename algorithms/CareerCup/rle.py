def rle(myStr):
    count = 1
    result = []
    size = len(myStr)
    idx = 1
    last = myStr[0]

    while idx <= size:
        print idx
        if idx < size and last == myStr[idx]:
            count += 1
        else:
            result.extend([str(count), last])
            count = 1

        if idx < size:
            last = myStr[idx]
        idx+=1

    return ''.join(result)

if __name__ == '__main__':
    myStr='aaaggbbbbbcd'
    print rle(myStr)
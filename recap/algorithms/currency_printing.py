def get_chunck(aStr):
    while aStr:
        yield aStr[-3:]
        aStr = aStr[:-3]

def get_format(aStr):
    r = aStr
    f= '00'
    if '.' in aStr:
        r,f = aStr.split('.')

    value = ''
    for i in get_chunck(r):
        print i
        if value :
            value = '{0},{1}'.format(i,value)
        else:
            value = i
    print value
    return '{0}.{1}'.format(value,f)


if __name__ == '__main__':
    aStr = '12323432.20'
    print get_format(aStr)
def wordsSplit(myStr, k):
    while myStr:
        yield myStr[-k:]
        myStr = myStr[:-k]

def printing(money):
    myStr = str(money)
    a = b = 0
    if '.' in myStr:
        a,b = myStr.split('.')
    else:
        a,b = str(money),0
    result = ''
    if b:
        result = '.{0}'.format(b)

    if len(a) >= 3:
        result = '{0}{1}'.format(a[-3:],result)

    newStr = a[:-3]

    for i in wordsSplit(newStr, 2):
        result = '{0},{1}'.format(i, result)

    return result

if __name__ == '__main__':
    print printing(2211.1)


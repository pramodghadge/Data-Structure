def get_number(myStr):
    if myStr == 'I':
        return 1
    elif myStr == 'V':
        return 5
    elif myStr == 'X':
        return 10
    else:
        return -1

def romanToDecimal(myStr):
    idx = 0
    result = 0
    while idx < len(myStr):
        val  = get_number(myStr[idx])
        if idx+1 < len(myStr):
            nextVal = get_number(myStr[idx+1])
            if val < nextVal:
                result = result + (nextVal-val)
                idx = idx + 2
            else:
                result = result + val
                idx += 1
        else:
            result += val
            idx += 1
    return result

if __name__ == '__main__':
    print romanToDecimal('XI')
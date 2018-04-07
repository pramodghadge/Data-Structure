def braket_matching(S):
    count = 0
    last = None
    aList = []

    for i, v in enumerate(S):
        if i == 0:
            aList.append(v)
        else:
            if len(aList) >= 1:
                last = aList[-1]
            if v == last:
                aList.append(v)
            elif last == '(' and v == ')':
                aList.pop()
                count += 1
            elif last == ')' and v == '(':
                aList.append(v)

    return count + len(aList)




if __name__ == '__main__':
    aStr = '(('
    aStr = '((()))(()(('
    # aStr = '(())'
    aStr = '))003())943))'
    print braket_matching(aStr)

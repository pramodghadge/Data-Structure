def bracket_balancing(myStr):
    aList = []

    for v in myStr:
        if v in ['(', '{', '[']:
            aList.append(v)
        elif v in [')', '}', ']']:
            if len(aList) > 0:
                last = aList.pop()
                if v == ')' and last != '(':
                    return False
                elif v == '}' and last != '{':
                    return False
                elif v == ']' and last != '[':
                    return False
            else:
                return False

    if len(aList) > 0:
        return False
    return True
if __name__ == '__main__':
    aStr = '((()))()'
    print bracket_balancing(aStr)
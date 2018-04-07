def bracket_balancing(myStr):
    myStack = []
    for ch in list(myStr):
        # print myStack
        if ch == '(' or ch == '{' or ch == '[':
            myStack.append(ch)
        elif ch == ')' or ch == '}' or ch == ']':
            if not myStack:
                return False
            # print myStack
            lastChr = myStack.pop()
            c = None
            if lastChr == '(':
                c = ')'
            elif lastChr == '{':
                c = '}'
            elif lastChr == '[':
                c = ']'
            if ch != c:
                print ch, lastChr
                return False

    if myStack:
        return False
    return True

if  __name__ == '__main__':
    myStr = '(a{b[n]m}j)[Na]'
    print bracket_balancing(myStr)
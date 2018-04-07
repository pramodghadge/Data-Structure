

def isPalindrome(mySubStr):
    if mySubStr == mySubStr[::-1]:
        return True
    return False

def find_palindrome(myStr, low, high, i ):
    if (high -low) >= 2:
        if isPalindrome(myStr[low:high]):
            return myStr[low:high]
        else:
            if i%2 == 0:
                low += 1
            else:
                high -= 1
            i += 1
            return find_palindrome(myStr, low, high, i)

if __name__ == '__main__':
    myStr = 'AABCDCBAD'
    myStr = 'ABAkkCD'
    print find_palindrome(myStr, 0, len(myStr), 0)
'''
Given a string, add some characters to the from of it so that it becomes a palindrome. E.g.1) If input is "abc" then
"bcabc" should be returned. 2) input -> "ab" output -> "bab" 3) input -> "a" output -> "a"
'''


def create_palindrome(myStr):
    return myStr[1:][::-1] + myStr

if __name__ == '__main__':
    print create_palindrome('abcd')
    data = create_palindrome('abcd')
    print data == data[::-1]
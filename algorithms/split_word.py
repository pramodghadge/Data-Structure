def split_word(aStr, k):
    # if len(aList) <= k:
    #     yield aList
    # yield aList[:k]
    # split_word(aList[k:], k)
    while aStr:
        yield aStr[:k]
        aStr = aStr[k:]


if __name__ == '__main__':
    for i in split_word('abcefgijklmn', 3):
        print i
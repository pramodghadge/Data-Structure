def findSubString(myStr, needle):
    if myStr is None or needle is None:
        return None

    i = j = 0
    startPos = 0

    size = len(myStr)

    while i < size:
        if myStr[i] == needle[j]:
            nSize = len(needle)
            startPos = i

            while i+1 < size and j+1 < nSize:
                if myStr[i+1] != needle[j+1]:
                    return None
                else:
                    i += 1
                    j += 1
            return startPos, i
        else:
            i += 1

    return None


if __name__ == '__main__':
    print findSubString('abcde', 'a')
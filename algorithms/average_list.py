
def get_average(aList, k):
    i = 0
    size = len(aList)
    result = []
    while i < size :
        maxOut = i+k
        if maxOut < size:
            print aList[i:maxOut], sum(aList[i:maxOut]),  sum(aList[i:maxOut])/k
            result.append(sum(aList[i:maxOut]) / k)
        i += 1

    return result


if __name__ == '__main__':
    aList= [1,2,3,4,5,6,7,8,9]
    print get_average(aList, 3)

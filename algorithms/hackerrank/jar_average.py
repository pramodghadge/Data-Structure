def getAverage(aInput):
    jars = 0
    myContainer = None
    for i in aInput:
        if len(i) == 2:
            jars = i[0]
            myContainer = [0] * jars
        else:
            lowIdx, highIdx, val = i
            lowIdx -= 1
            for j in range(lowIdx, highIdx):
                myContainer[j] += val

    return sum(myContainer) / jars





if __name__ == '__main__':
    aInput = [
        (5,3),
        (1,2,100),
        (2,5,100),
        (3,4,100)
    ]

    print getAverage(aInput)
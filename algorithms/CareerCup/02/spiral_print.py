def printSpiral(aList):
    noOfColumns = len(aList[0])
    noOfRows = len(aList)

    leftColumn = 0
    rightColumn = noOfColumns -1
    topRow = 0
    bottomRows = noOfRows - 1

    result = []

    while leftColumn <= rightColumn and topRow <= bottomRows:
        for i in range(leftColumn, rightColumn+1):
            result.append(aList[topRow][i])

        topRow += 1

        for i in range(topRow, bottomRows+1):
            result.append(aList[i][rightColumn])

        rightColumn -= 1


        for i in range(rightColumn,leftColumn-1, -1):
            result.append(aList[bottomRows][i])

        bottomRows -= 1

        for i in range(bottomRows, topRow - 1, -1):
            result.append(aList[i][leftColumn])

        leftColumn += 1

    return result

if __name__ == '__main__':
    aList=[[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]

    print printSpiral(aList)
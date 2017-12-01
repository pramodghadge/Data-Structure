#


def print_spiral(inputMatrix):
    numOfRows = len(inputMatrix)
    numofClm = len(inputMatrix[0])


    topRow = 0
    btmROw = numOfRows-1
    leftClm = 0
    rightClm = numofClm-1

    result = []
    while topRow <= btmROw and leftClm <= rightClm:
        for i in range(leftClm, rightClm+1):
            result.append(inputMatrix[topRow][i])

        topRow += 1

        for i in range(topRow, btmROw+1):
            result.append(inputMatrix[i][rightClm])

        rightClm -= 1

        for i in range(rightClm, leftClm-1, -1):
            result.append(inputMatrix[btmROw][i])

        btmROw -= 1

        for i in range(btmROw, topRow-1, -1):
            result.append(inputMatrix[i][leftClm])

        leftClm +=1

    print result

if __name__ == '__main__':
    inputMatrix = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]
    print_spiral(inputMatrix)
def spiral_matrix(aMatrix):
    noofRows = len(aMatrix)
    noOfColumns = len(aMatrix[0])

    topRow = 0
    bottomRow = noofRows-1
    leftClm = 0
    rightClm = noOfColumns -1

    results = []
    while topRow <= bottomRow and leftClm <= rightClm:
        for i in range(leftClm, rightClm+1):
            results.append(aMatrix[topRow][i])

        topRow += 1

        for i in range(topRow, bottomRow+1):
            results.append(aMatrix[i][rightClm])

        rightClm -= 1

        for i in range(rightClm, leftClm-1, -1):
            results.append(aMatrix[bottomRow][i])

        bottomRow -= 1

        for i in range(bottomRow, topRow-1, -1):
            results.append(aMatrix[i][leftClm])

        leftClm += 1
    return results

if __name__ == '__main__':
    inputMatrix = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]
    print spiral_matrix(inputMatrix)
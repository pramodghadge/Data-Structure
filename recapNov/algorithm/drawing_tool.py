def printShape(out, line, filling):
    out.write(line)
    print line
    for i in filling:
        out.write(i)
        print i
    out.write(line)
    print line

def processInput(inputFile, outFile ):
    lines = None
    with open(inputFile) as fh:
        lines = fh.readlines()

    lines = map(lambda x: x.strip(), lines)
    if not lines:
        return

    with open(outFile, 'w') as out:
        width, height = lines[0].split()[1:]
        width = int(width)
        height = int(height)
        # H line
        hLine = drawHLine(width+2)
        filling = getInternal(width,height)
        printShape(out, hLine,filling)

        for row in lines[1:]:
            filling = fillUp(width, height, row, filling)
            printShape(out, hLine, filling)


def drawHLine(width, lineChar='-'):
    return ''.join(map(str, [lineChar] * width))

def getInternal(width, height, lineChar='|'):
    result = []
    for i in range(1, height+1):
        lineSpacing = " " * width
        result.append("{0}{1}{0}".format(lineChar, lineSpacing))
    return result


def fillUp(width, height, inputRec, result, lineChar='|'):
    dType = None
    if inputRec:
        rec =  inputRec.split()
        dType = rec[0]
    x1 = y1 = x2 = y2 = None
    if dType in {'L', 'R'}:
        x1 = int(rec[1])
        y1 = int(rec[2])
        x2 = int(rec[3])
        y2 = int(rec[4])

    for i in range(1, height+1):
        aList = list(result[i - 1])

        if i >= y1 and i <= y2:
            for j in range(x1, x2+1):
                aList[j] = 'x'
            result[i - 1] = "".join(aList)
        if dType == 'B':
            result[i - 1] = ''.join(map(lambda x: 'o' if x == " " else x, aList))
    return result


if __name__ == '__main__':
    input = processInput("input.txt", 'out1.txt')

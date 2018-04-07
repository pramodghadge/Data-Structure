

def printDiamond(inputSize=6):
    for i in range(inputSize) + list(reversed(range(inputSize-1))):
        print '{0}{1}'.format(" " * (inputSize-i-1), '*' * (i*2+1))

if __name__ == '__main__':
    printDiamond()

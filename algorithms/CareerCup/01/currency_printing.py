def currency_printing(aDigit, Indian=True):
    counter = 0
    modby = 3
    aList = []
    while aDigit > 0:
        if counter != 0  and counter == modby:
            aList.append(',')
            if Indian:
                modby = counter + 2
            else:
                modby = counter + 3

        aList.append(str(aDigit % 10))
        aDigit /= 10
        counter += 1

    return ''.join(aList[::-1])

if __name__ == '__main__':
    print currency_printing(123234, True)




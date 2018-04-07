def formatNumber(aNumber, indianFormat=True):
    total_processed = 0
    result = ''
    modBy = 3

    while aNumber > 0:
        if total_processed != 0 and total_processed == modBy:
            result += ","
            if indianFormat:
                modBy = total_processed + 2
            else:
                modBy = total_processed + 3
        result += str(aNumber % 10)
        total_processed += 1
        aNumber /= 10

    print result[::-1]

if __name__ == '__main__':
    formatNumber(546767, indianFormat=False)
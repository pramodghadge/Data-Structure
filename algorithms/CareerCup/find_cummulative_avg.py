def find_cum_avg(aList, k=3):
    low = 0
    high = low + k
    size = len(aList)

    while high <= size:
        avg = sum(aList[low:high]) / k
        print avg, aList[low:high]
        low +=1
        high = low + k


if __name__  == '__main__':
    find_cum_avg([1, 2, 3, 4, 5, 6, 7, 8])
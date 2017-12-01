def quick_sort(aList, low, high):
    if low < high:
        split_point = partition(aList, low, high)
        quick_sort(aList, low, split_point-1)
        quick_sort(aList, split_point+1, high)


def partition(aList, low, high):
    pivot = low
    left_mark = low+1
    right_mark = high

    done = False

    while not done:
        while left_mark <= right_mark and aList[left_mark] <= aList[pivot]:
            left_mark += 1

        while right_mark >= left_mark and aList[right_mark] >= aList[pivot]:
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            aList[left_mark], aList[right_mark] = aList[right_mark], aList[left_mark]

    aList[low], aList[right_mark] = aList[right_mark], aList[low]
    return right_mark

if __name__ == '__main__':
    aList = [2, 4, 0, 23, 5, 20, 17, 16,3,19]
    quick_sort(aList, 0, len(aList)-1)
    print aList
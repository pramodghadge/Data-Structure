def quick_sort(aList, left, right):
    if left < right:
        split_point = partition(aList, left, right)
        quick_sort(aList, left, split_point-1)
        quick_sort(aList, split_point+1, right)


def partition(aList, left, right):
    pivot = left
    left_mark = left+1
    right_mark = right

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

    aList[left], aList[right_mark] = aList[right_mark], aList[left]
    return right_mark


if __name__ == '__main__':
    aList = [23,3,5,34,65,20,10]
    quick_sort(aList, 0, len(aList)-1)
    print aList
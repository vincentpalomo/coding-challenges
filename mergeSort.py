import random

numbers = [random.randint(0, 100) for _ in range(10)]

print('random numbers array', numbers)


def mergeSort(numbers):
    # get lenght of input array
    inputLenght = len(numbers)

    # if array is less than 2 elements, it is already sorted
    if inputLenght < 2:
        return numbers

    # get midpoint of array
    mid = inputLenght // 2

    # create two empty arrays, one for left of midpoint and one for right of midpoint
    left = [0] * mid
    right = [0] * (inputLenght - mid)

    print('two empty arrays', left, right)

    # fill left array
    for i in range(mid):
        left[i] = numbers[i]

    # fill right array
    for i in range(mid, inputLenght):
        right[i - mid] = numbers[i]

    print('left and right filled with values', left, right)

    # recursively call mergeSort function to sort the left and right sub-arrays
    left = mergeSort(left)
    right = mergeSort(right)

    # merge the sorted left and right sub-arrays back into the original 'numbers' array
    merge(numbers, left, right)

    return numbers


def merge(numbers, left, right):

    # get length of left and right sub arrays
    leftSize = len(left)
    rightSize = len(right)

    # init pointers for left, right and numbers array
    i = 0
    j = 0
    k = 0

    # merge the two sub arrays in ascending order
    # if the current element in left sub-array is smaller, add it to the main array
    # if the current element in right sub-array is smaller, add it to the main array
    while i < leftSize and j < rightSize:
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    # after the previous loop, one of the sub-arrays may still have some elements left.
    # add any remaining elements from the left sub-array to the main array
    while i < leftSize:
        numbers[k] = left[i]
        i += 1
        k += 1
    # add any remaining elements from the right sub-array to the main array
    while j < rightSize:
        numbers[k] = right[j]
        j += 1
        k += 1


ret = mergeSort(numbers)
print('mergeSort: ', ret)

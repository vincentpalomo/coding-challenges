import random

numbers = [random.randint(0, 100) for _ in range(10)]

print('random numbers array', numbers)


def mergeSort(numbers):
    # get lenght of input array
    inputLenght = len(numbers)

    # smallest array will be less than 2
    if inputLenght < 2:
        return numbers

    # get midpoint of array
    mid = inputLenght // 2
    left = [0] * mid
    right = [0] * (inputLenght - mid)

    print(left, right)


ret = mergeSort(numbers)
print('mergeSort: ', ret)

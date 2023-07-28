# O(n log n) time | O(n) space
def sortedSquaredArrayBrute(array):
    # create an empty array with the length of input array filled with 0
    sortedSqaures = [0 for _ in array]

    # square each element in the input array and store the squared values in sorted Array
    for i in range(len(array)):
        value = array[i]
        sortedSqaures[i] = value * value

    # sort the squared values in ascending order
    sortedSqaures.sort()

    return sortedSqaures


ret = sortedSquaredArrayBrute([-2, 1, 3, 9, 6])
print(ret)

# 0(n) time | O(n) space


def sortedSquaredArray(array):
    # create an empty array with lenght of input array with 0
    sortedSquares = [0 for _ in array]

    # init two pointers, start at beginning of array and end at the end
    start = 0
    end = len(array) - 1

    # traverse the array from the end to the beginning
    for i in reversed(range(len(array))):
        # get values of elements at start and end
        small = array[start]
        large = array[end]

        # compare the absolute values and square the larger one
        if abs(small) > abs(large):
            sortedSquares[i] = small * small
            # move start pointer to the right
            start += 1
        else:
            sortedSquares[i] = large * large
            # move end pointer to the left
            end -= 1

    return sortedSquares


ret = sortedSquaredArray([-4, 1, 2, 5, 9, 10])
print(ret)

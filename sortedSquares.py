
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

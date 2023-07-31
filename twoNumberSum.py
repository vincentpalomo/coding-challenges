def twoNumberSum(array, target):
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == target:
            print('Answer: ', array[left], array[right])
            return [array[left], array[right]]
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1


twoNumberSum([1, 3, -4, -5, 10], 13)


def twoNumberSumHash(array, target):
    nums = {}
    for num in array:
        if target - num in nums:
            return [target - num, num]
        else:
            nums[num] = True
    return []


ret = twoNumberSumHash([1, 3, -4, -5, 10], 13)
print('Hash return', ret)

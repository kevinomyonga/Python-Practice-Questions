# Author: Kevin Omyonga
# Date: 02-June-2022

# Triplet Array Which Sums to Target

# Question:
# Write a function that takes in a target sum and an array of positive integers.
# The function should return a list of triplets whose sum is equal to the target sum.
# If no triplet exists, return an empty list.
#

def tripletSum(array, targetSum):
    array.sort()
    ans = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                ans.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1

    return ans


# Example 1
print("Example 1 (Target Sum = 24):")
print(tripletSum([12, 3, 4, 1, 6, 9], 24))

# Example 2
print("Example 2 (Target Sum = 9):")
print(tripletSum([1, 2, 3, 4, 5], 9))

def solveRecursively(nums, operation):
    if(len(nums)) == 1:
        return nums[0]
    else:
        left = solveRecursively(nums[:len(nums)//2], min)
        right = solveRecursively(nums[len(nums)//2:], max)
        return operation(
            left,
            right
        )

class Solution:
    def minMaxGame(self, nums):
        return solveRecursively(nums, min)
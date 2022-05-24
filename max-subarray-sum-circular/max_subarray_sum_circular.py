def coallesce(nums):
    results = [nums[0]]
    for i in range(1, len(nums)):
        signsMatch = ((nums[i] < 0) == (nums[i-1] < 0))
        if signsMatch:
            results[-1] += nums[i]
        else:
            results.append(nums[i])
    return results

def generateResults(nums):
    results = [None] * len(nums)
    results[0] = nums[0]
    
    for i in range(1, len(nums)):
        results[i] = nums[i] + max(results[i-1], 0)
    return results

def maxSubarray(nums):
    return max(generateResults(nums))

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNums = max(nums)
        nums = coallesce(nums)
        if len(nums) == 1:
            return maxNums if nums[0] < 0 else nums[0]

        unwrapped = maxSubarray(nums)

        biggestNegatives = maxSubarray([0-n for n in nums])

        wrapped = sum(nums) + biggestNegatives

        return max([
            maxNums,
            unwrapped,
            wrapped
        ])


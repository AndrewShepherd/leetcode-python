class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        mins = [None] * len(nums)
        mins[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            mins[i] = min(nums[i], mins[i+1])
        maxes = [None] * len(nums)
        maxes[0] = nums[0]
        for i in range(1, len(nums)):
            maxes[i] = max(nums[i], maxes[i-1])
        results = [None] * len(nums)
        results[-1] = maxes[-1]
        for i in range(len(nums)-2, -1, -1):
            results[i] = results[i+1] if maxes[i] > mins[i+1] else maxes[i]

        return results

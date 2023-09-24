class Solution:
    def countWays(self, nums) -> int:
        nums.sort()
        if not nums:
            return 0
        result = 0
        if nums[0] > 0:
            result += 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if (nums[i-1] < i) and nums[i] > i:
                result += 1
        if nums[-1] < len(nums):
            result += 1
        return result

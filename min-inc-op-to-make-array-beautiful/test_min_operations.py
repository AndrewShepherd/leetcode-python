class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        if len(nums) <= 3:
            return max(k - max(nums), 0)
        decisions = [max(k - n, 0) for n in nums[:3]]
        for i in range(3, len(nums)):
            n = nums[i]
            decisions = decisions[1:] + [min(decisions) + max(k-n, 0)]
        return min(decisions)

class Solution:
    def minimumOperations(self, nums) -> int:
        c = 0
        nums = [n for n in nums if n > 0]
        while nums:
            m = min(nums)
            nums = [n-m for n in nums if n > m]
            c += 1
        return c
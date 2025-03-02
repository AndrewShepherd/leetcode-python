import math

class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        result = 0
        target_min = 0 - math.inf
        for n in nums:
            target_min = max(target_min, n - k)
            if target_min <= n + k:
                target_min += 1
                result += 1
        return result


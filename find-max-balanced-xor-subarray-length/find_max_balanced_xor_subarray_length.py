class Solution:
    def maxBalancedSubarray(self, nums: list[int]) -> int:
        lookup = dict()
        agg = (0, 0)
        result = 0
        for i,n in enumerate(nums):
            agg = (agg[0] + (1 if (n % 2) else -1), agg[1] ^ n)
            if (agg == (0, 0)):
                result = i + 1
            else:
                complement = (0 - agg[0], agg[1])
                if complement in lookup:
                    this_result = i - lookup[complement]
                    result = max(result, this_result)
                if not (complement in lookup):
                    lookup[complement] = i
        return result

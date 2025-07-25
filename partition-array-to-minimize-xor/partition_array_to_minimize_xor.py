from math import inf
from functools import cache

class Solution:
    def minXor(self, nums: list[int], k: int) -> int:
        @cache
        def solve(start_index, k_value):
            aggregate = 0
            if (k_value == 1):
                for i in range(start_index, len(nums)):
                    aggregate ^= nums[i]
                return aggregate          
            result = inf
            max_length = (len(nums) - start_index - k_value + 1)

            for i in range(start_index, min(start_index + max_length, len(nums))):
                aggregate ^= nums[i]
                this_result = max(aggregate, solve(i+1, k_value-1))
                result = min(result, this_result)
            return result


        return solve(0, k)
  

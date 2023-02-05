import heapq
import math
from functools import cache

class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:

        @cache
        def solve_recursively(start_index, k):
            if k == 0:
                return None
            if (len(nums)-start_index+1)//2 < k:
                return None
            if k == 1:
                return min(nums[start_index:])
            
            
            value_with_start_index = max(nums[start_index], solve_recursively(start_index + 2, k - 1))
            value_without_start_index = solve_recursively(start_index + 1, k)

            best_result = value_with_start_index

            if value_without_start_index:
                if best_result:
                    best_result = min(best_result, value_without_start_index)
                else:
                    best_result = value_without_start_index

            return best_result


        return solve_recursively(0, k)

        

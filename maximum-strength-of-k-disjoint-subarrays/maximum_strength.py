from functools import cache
from math import inf;

class Solution:
    def maximumStrength(self, nums: list[int], k_total: int) -> int:

        sums = nums[:]
        for i in range(1, len(sums)):
            sums[i] += sums[i-1]

        @cache 
        def max_subarray_sum(start: int, end_exclusive: int):
            result = 0 - inf
            for i in range(start, end_exclusive):
                sum_before_start = 0 if i == 0 else sums[i-1]
                for j in range(i+1, end_exclusive+1):
                    # what is range i::j
                    sum_at_end = sums[j-1]
                    this_result = sum_at_end - sum_before_start
                    result = max(result, this_result)
            return result
        
        @cache 
        def min_subarray_sum(start: int, end_exclusive: int):
            result = inf
            for i in range(start, end_exclusive):
                sum_before_start = 0 if i == 0 else sums[i-1]
                for j in range(i+1, end_exclusive+1):
                    # what is range i::j
                    sum_at_end = sums[j-1]
                    this_result = sum_at_end - sum_before_start
                    result = min(result, this_result)
            return result

        @cache
        def solve_dp(end_exclusive: int, k: int):
            if k == 1:
                return max_subarray_sum(0, end_exclusive) * k_total
            if k == end_exclusive:
                result = 0
                toggle = 1
                for i in range(k):
                    n = nums[i]
                    k_multiplier = (k_total - i)
                    result += n * k_multiplier * toggle
                    toggle *= -1
                return result
            # if k is odd, then multiply by 1
            start_index = k-1
            best_result = 0 - inf         
            if k % 2 == 0: # if k is even, then multiply by -1 (we want it small)
                for i in range(start_index, end_exclusive):
                    dp_result = solve_dp(i, k - 1)
                    m_s_s = min_subarray_sum(i, end_exclusive)
                    x_multiplier = (k_total - k + 1)
                    this_result = dp_result - x_multiplier * m_s_s
                    best_result = max(this_result, best_result)
            else:
                for i in range(start_index, end_exclusive):
                    dp_result = solve_dp(i, k - 1)
                    m_s_s = max_subarray_sum(i, end_exclusive)
                    x_multiplier = (k_total - k + 1)
                    this_result = dp_result + x_multiplier * m_s_s
                    best_result = max(this_result, best_result)
            return best_result 
        return solve_dp(len(nums), k_total)

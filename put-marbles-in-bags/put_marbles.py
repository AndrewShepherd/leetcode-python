import math
from functools import cache

class Solution:

    def putMarbles(self, weights: list[int], k: int) -> int:
        
        @cache
        def solve_recursive(up_to, k, pick, initial):
            if k == 1:
                return weights[0] + weights[up_to-1]
            if up_to == k:
                return sum(weights[:up_to]) * 2
            final_partition_possible_length = range(1,up_to-k+2)
            value = initial
            for l in final_partition_possible_length:
                these_ends = (weights[up_to-l], weights[up_to-1])
                sub_value = solve_recursive(up_to-l, k-1, pick, initial)
                this_result = sub_value +sum(these_ends)
                value = pick(value, this_result)
            return value


        max_result = solve_recursive(len(weights), k, max, 0)
        min_result = solve_recursive(len(weights), k, min, math.inf)
        return max_result - min_result


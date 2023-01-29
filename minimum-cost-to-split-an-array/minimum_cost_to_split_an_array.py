from collections import Counter
import math



class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        optimal_solutions = [0] * len(nums)
        number_counts = [[0] * len(nums) for _ in range(len(nums))]
        trimmed_totals = [0] * len(nums)
        for i,n in enumerate(nums):
            for j in range(i+1):
                tc = number_counts[j]
                increment_index = nums[i]
                tc[increment_index] += 1
                if tc[increment_index] > 2:
                    trimmed_totals[j] += 1
                elif tc[increment_index] == 2:
                    trimmed_totals[j] += 2
            best_result = math.inf
            for starting_point in range(i+1):
                tv = trimmed_totals[starting_point] + (0 if starting_point == 0 else optimal_solutions[starting_point-1]) + k
                best_result = min(tv, best_result)
            optimal_solutions[i] = best_result
        return optimal_solutions[-1]

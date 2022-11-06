from collections import defaultdict
import math

class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        d = defaultdict(lambda: 0)
        for num, cost in zip(nums, cost):
            d[num] += cost
        nums_and_costs = sorted(d.items())

        upward_result = [0] * len(nums_and_costs)
        cost_per_step = nums_and_costs[0][1]
        for i in range(1, len(nums_and_costs)):
            n, cost = nums_and_costs[i]
            steps = n-nums_and_costs[i-1][0]
            upward_result[i] = upward_result[i-1] + steps * cost_per_step
            cost_per_step += cost

        downward_result = [0] * len(nums_and_costs)
        cost_per_step = nums_and_costs[-1][1]

        min_result = upward_result[-1]
        for i in range(len(nums_and_costs)-2, -1, -1):
            n, cost = nums_and_costs[i]
            steps = nums_and_costs[i+1][0]-n
            downward_result[i] = downward_result[i+1] + steps * cost_per_step
            cost_per_step += cost
            min_result = min(min_result, downward_result[i] + upward_result[i])

        return min_result


from collections import defaultdict
import math
from functools import cache

def local_min(left, right_exclusive, calc):
    mid = left + (right_exclusive-left)//2
    mid_value = calc(mid)
    left_value = math.inf if mid == 0 else calc(mid-1)
    right_value = math.inf if mid+1 >= right_exclusive else calc(mid+1)
    if mid_value < left_value and mid_value < right_value:
        return mid
    elif mid_value < left_value:
        return local_min(mid, right_exclusive, calc)
    else:
        return local_min(left, mid, calc)

class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        d = defaultdict(lambda: 0)
        for num, cost in zip(nums, cost):
            d[num] += cost
        nums_and_costs = sorted(d.items())

        @cache
        def calculate_cost(index):
            n = nums_and_costs[index][0]
            return sum([abs(num-n)*cost for num,cost in nums_and_costs])

        best_index = local_min(0, len(nums_and_costs), calculate_cost)
        return calculate_cost(best_index)

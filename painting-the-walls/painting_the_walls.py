import math
from collections import defaultdict

class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        dp = defaultdict(lambda: math.inf)
        dp[time[0]] = cost[0]
        dp[-1] = 0
        best_result = math.inf
        for i in range(1, len(cost)):
            c = cost[i]
            t = time[i]
            dp2 = defaultdict(lambda: math.inf)
            remaining_walls_after_this_one = len(cost) - i - 1
            for remaining_time, cost_so_far in dp.items():
                remaining_time_if_we_paint = remaining_time + t
                total_cost_if_we_paint = cost_so_far + c
                if total_cost_if_we_paint < best_result:
                    if remaining_walls_after_this_one <= remaining_time_if_we_paint:
                        best_result = min(best_result, total_cost_if_we_paint)
                    else:
                        dp2[remaining_time_if_we_paint] = min(dp2[remaining_time_if_we_paint], total_cost_if_we_paint)
                remaining_time_if_we_dont_paint = remaining_time - 1
                if remaining_walls_after_this_one <= remaining_time_if_we_dont_paint:
                    best_result = min(best_result, cost_so_far)
                else:
                    dp2[remaining_time_if_we_dont_paint] = min(dp2[remaining_time_if_we_dont_paint], cost_so_far)
            dp = dp2
        return best_result

        
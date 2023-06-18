import math
from functools import cache

class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        costs_and_time = list(zip(cost, time))
        costs_and_time.sort(key=lambda t:(t[0], 0-t[1]))
        paid_index = 0
        free_index = len(costs_and_time)
        initial_total_cost = 0
        while(free_index > paid_index):
            initial_total_cost += costs_and_time[paid_index][0]
            free_index -= costs_and_time[paid_index][1]
            paid_index += 1

        @cache
        def solve_recursively(start_index, minimum_time, maximum_cost):
            if start_index >= len(costs_and_time):
                if minimum_time > 0:
                    return None
                else:
                    return 0
            if maximum_cost < 0:
                return None
            
            if minimum_time < 0 and 0-minimum_time >= len(costs_and_time) - start_index:
                return 0
            best_result = math.inf
            cost, time = costs_and_time[start_index]

            paid_subresult = solve_recursively(start_index + 1, minimum_time - time, maximum_cost - cost)
            cost_if_we_pay_for_it = (cost + paid_subresult) if paid_subresult != None else None
            unpaid_subresult = solve_recursively(
                start_index + 1, 
                minimum_time + 1, 
                min(maximum_cost, cost_if_we_pay_for_it if cost_if_we_pay_for_it != None else math.inf)
            )
            cost_if_we_dont_pay_for_it = unpaid_subresult
            if cost_if_we_pay_for_it != None:
                best_result = cost_if_we_pay_for_it
            if cost_if_we_dont_pay_for_it != None:
                best_result = min(best_result, cost_if_we_dont_pay_for_it)
            return best_result if best_result != math.inf else None
                
        result = solve_recursively(0, 0, initial_total_cost)
        if result == None:
            return initial_total_cost
        else:
            return min(initial_total_cost, result)

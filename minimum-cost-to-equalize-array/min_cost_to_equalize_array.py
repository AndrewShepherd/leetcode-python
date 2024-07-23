from collections import Counter, defaultdict
import math

modulo = 10**9 + 7

def solve_for_target(nums: list[int], cost1: int, cost2: int, target: int, original_len: int) -> int:
        increments_required = sum([target - n for n in nums])
        if cost1*2 <= cost2:
            return increments_required * cost1
        if increments_required == 0:
            return 0
        
        right_index = len(nums) 
        total_diff = 0
        while(True):
            right_index -= 1
            total_diff_next = total_diff + target - nums[right_index]
            if total_diff_next > increments_required//2:
                break
            total_diff = total_diff_next

        # Now add total_diff to nums[0:right_index+1]
        left_receiver_length = right_index+1
        new_sum = sum(nums[:left_receiver_length]) + total_diff
        avg = new_sum // left_receiver_length
        remainder = new_sum % left_receiver_length


        if (remainder == 0):
            values_and_counts = [(avg, left_receiver_length)]
        elif avg+1 == target:
            values_and_counts = [(avg, left_receiver_length - remainder)]
        else:
            values_and_counts = [
                (avg, left_receiver_length - remainder),
                (avg + 1, remainder)
            ]
        
        running_cost = total_diff * cost2

        if len(values_and_counts) == 1:
            v, c = values_and_counts[0]
            if c == 1:
                return running_cost + (target-v) * cost1
            else:
                sub_result = solve_for_target(
                    [v] * c,
                    cost1,
                    cost2,
                    target,
                    original_len
                )
                return running_cost + sub_result
        else:
            remaining_sequence = [
                *([values_and_counts[0][0]] * values_and_counts[0][1]),
                *([values_and_counts[1][0]] * values_and_counts[1][1]),
            ]
            s_result = solve_for_target(
                remaining_sequence,
                cost1,
                cost2,
                target,
                original_len
            )
            return running_cost + s_result
            

def get_ceiling_target(max_score: int, nums_sum: int, nums_len: int, cost2: int) -> int:
    available_double_increments = math.ceil(max_score / cost2)
    new_sum = nums_sum + available_double_increments * 2
    return math.ceil(new_sum / nums_len)

class Solution:
    def minCostToEqualizeArray(self, nums: list[int], cost1: int, cost2: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        if len(nums) == 2:
            return (nums[1] - nums[0]) * cost1 % modulo
        max_value = nums[-1]
        nums_sum = sum(nums)
        if cost1*2 <= cost2:
            return (max_value * len(nums) - nums_sum) * cost1 % modulo

        best_result_so_far = solve_for_target(nums, cost1, cost2, max_value, len(nums))
        ceiling_target = get_ceiling_target(best_result_so_far, nums_sum, len(nums), cost2)
        next_target = max_value
        while True:
            next_target += 1
            if next_target > ceiling_target:
                break
            current_result = solve_for_target(nums, cost1, cost2, next_target, len(nums))
            if current_result >= best_result_so_far:
                print(f'increments = {next_target-max_value-1}\n')
                break
            best_result_so_far = current_result
            ceiling_target = get_ceiling_target(best_result_so_far, nums_sum, len(nums), cost2)

        return best_result_so_far % modulo






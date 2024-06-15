from collections import Counter, defaultdict

modulo = 10**9 + 7

def tricky_calculation(distance_behind, quantity, cost1, cost2):
    if quantity == 2:
        return distance_behind * cost1

    x = distance_behind // (quantity - 2)
    result = x * cost2
    target = distance_behind + x
    lowest_value = x * (quantity-2)
    result = x*cost2 + (target-lowest_value)*cost1
    return min(result, distance_behind * cost1)


def calculate_cost(target, nums, cost1, cost2):
    running_total = 0
    left_over = target
    for n in nums:
        left_over, n = max(left_over,n), min(left_over,n)
        running_total += (target - left_over) * cost2
        left_over = n + target - left_over
    return running_total + (target - n) * cost1


def add(n, q, amount):
    if amount % q == 0:
        return [((n + amount // q), q)]
    else:
        total = n*q + amount
        average = total // q
        left_over = total % q
        return [
            (average, q-left_over),
            (average + 1, left_over)
        ]
    
def merge(l: list[tuple[int, int]]) -> list[tuple[int, int]]:
    d = defaultdict(lambda:0)
    for n, q in l:
        d[n] += q
    return sorted(d.items())


# x/(nums_length-1) + amount_behind = x
# amount_behind = x - x/(nums_length-1)
# amount_behind(nums_length-1) = x(nums_length-1) - x
# amound_behind(nums_length-1) = x(nums_length-1 - 1)
# amount_behind(nums_length-1) = x(nums_length-2)
# amount_behind(nums_length-1)/(nums_length-2) = x

class solve_with_one_item_left_result:

    def __init__(self, single_increments, double_increments, total_cost):
        self.single_increments = single_increments
        self.double_increments = double_increments
        self.total_cost = total_cost
        self.total_increments = single_increments + double_increments


def sove_with_one_item_left(amount_behind, nums_length, cost1, cost2) -> solve_with_one_item_left_result:
    cost_1_alone = amount_behind * cost1
    result_just_cost1 = solve_with_one_item_left_result(amount_behind, 0, cost_1_alone)
    if cost1 <= cost2:
        return result_just_cost1
    
    x = (amount_behind*(nums_length-1))//(nums_length-2)
    remainder = (amount_behind*(nums_length-1)) %(nums_length-2) 
    cost_2_factor = x * cost2
    cost_1_factor = remainder * cost1
    result_two_costs = solve_with_one_item_left_result(remainder, x, cost_2_factor + cost_1_factor)

    return result_just_cost1 if result_just_cost1.total_cost <= result_two_costs.total_cost else result_two_costs

class solve_for_target_result:
    def __init__(self, cost, actual_target):
        self.cost = cost
        self.actual_target = actual_target

def solve_for_target(nums: list[int], cost1: int, cost2: int, target: int, original_len: int) -> solve_for_target_result:
        increments_required = sum([target - n for n in nums])
        if cost1*2 <= cost2:
            return solve_for_target_result(increments_required * cost1, target)
        if increments_required == 0:
            return solve_for_target_result(0, target)
        
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
            if v == target:
                return solve_for_target_result(
                    running_cost,
                    target
                )
            elif c == 1:
                s_result = sove_with_one_item_left(
                    target - v,
                    original_len,
                    cost1,
                    cost2
                )
                return solve_for_target_result(
                    running_cost + s_result.total_cost, 
                    s_result.total_increments + v
                )
            else:
                sub_result = solve_for_target(
                    [v] * c,
                    cost1,
                    cost2,
                    target,
                    original_len
                )
                return solve_for_target_result(
                    running_cost + sub_result.cost,
                    sub_result.actual_target
                )
        else:
            if values_and_counts[1][0] == target:
                raise Exception(f"TODO: Apply the clever formula {values_and_counts}")
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
                return solve_for_target_result(
                    running_cost + s_result.cost, 
                    s_result.actual_target
                )


class Solution:
    def minCostToEqualizeArray(self, nums: list[int], cost1: int, cost2: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        if len(nums) == 2:
            return (nums[1] - nums[0]) * cost1 % modulo
        max_value = nums[-1]

        def solve_with_delta(delta):
            return solve_for_target(nums, cost1, cost2, max_value + delta, len(nums)).cost

        results = [solve_with_delta(n) for n in range(9809)]
        min_result = min(results)
        min_result_modded = min_result % modulo
        return min_result_modded





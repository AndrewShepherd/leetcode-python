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

def sove_with_one_item_left(amount_behind, nums_length, cost1, cost2) -> int:
    cost_1_alone = amount_behind * cost1
    if cost1 <= cost2:
        return cost_1_alone
    
    x = (amount_behind*(nums_length-1))//(nums_length-2)
    remainder = (amount_behind*(nums_length-1)) %(nums_length-2) 
    cost_2_factor = x * cost2
    cost_1_factor = remainder * cost1
    return min(cost_1_alone, cost_1_factor + cost_2_factor)

def transform(nums_and_counts: list[tuple[int, int]], cost1: int, cost2: int) -> tuple[int, list[tuple[int, int]]]:
    if len(nums_and_counts) == 2:
        left_num, left_count = nums_and_counts[0]
        right_num, right_count = nums_and_counts[1]
        if left_count > 1:
            total_increments_required = (right_num - left_num) * left_count
            double_additions = total_increments_required - total_increments_required % 2
            left_with_doubles = add(left_num, left_count, double_additions)
            return [double_additions * cost2, merge([*left_with_doubles, nums_and_counts[1]])]
        else:
            # THIS IS THE SPECIAL FORMULA
            m = right_num - left_num
            n = right_count
            x = (m*n)//(n-1)
            if (x == 0):
                raise Exception("TODO")
            else:
                left_num += x
                right_num += x//n
                if left_num == right_num:
                    return (x * cost2, [(left_num, left_count + right_count)])
                else:
                    raise Exception("TODO") 
    elif len(nums_and_counts) == 3:
        left_num, left_count = nums_and_counts[0]
        right_num, right_count = nums_and_counts[1]
        last_num, last_count = nums_and_counts[2]
        available = (last_num - right_num) * right_count
        required = (last_num - left_num) * left_count
        if (available < required) and left_count == 1:
            return (
                cost2 * available,
                [
                    (left_num + available, left_count),
                    (last_num, last_count + right_count)    
                ]
            )
        elif (available == required):
            raise Exception(f"TODO: {nums_and_counts}")
        elif (available > required):
            split_result = add(*nums_and_counts[1], required)
            return (
                cost2 * required,
                [
                    *split_result,
                    (last_num, last_count + left_count)
                ]
            )
            raise Exception(f"TODO: {nums_and_counts}")
        else:
            raise Exception(f"TODO: {nums_and_counts}")
    else:
        raise Exception("todo")
    return (0, [])


def solve_for_target(nums: list[int], cost1: int, cost2: int, target: int, original_len: int) -> int:

        increments_required = sum([target - n for n in nums])
        if cost1*2 <= cost2:
            return increments_required * cost1
        
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
            if values_and_counts[0][0] == target:
                return running_cost
            elif values_and_counts[0][1] == 1:
                return running_cost  + sove_with_one_item_left(
                    target - values_and_counts[0][0],
                    original_len,
                    cost1,
                    cost2
                )
            else:
                return running_cost + solve_for_target(
                    [values_and_counts[0][0]] * values_and_counts[0][1],
                    cost1,
                    cost2,
                    target,
                    original_len
                )
        else:
            if values_and_counts[1][0] == target:
                raise Exception(f"TODO: Apply the clever formula {values_and_counts}")
            else:
                return running_cost + solve_for_target(
                    [
                        *([values_and_counts[0][0]] * values_and_counts[0][1]),
                        *([values_and_counts[1][0]] * values_and_counts[1][1]),
                    ],
                    cost1,
                    cost2,
                    target,
                    original_len
                )
                raise Exception(f"Not handling this situation! {values_and_counts}")


class Solution:
    def minCostToEqualizeArray(self, nums: list[int], cost1: int, cost2: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        if len(nums) == 2:
            return (nums[1] - nums[0]) * cost1
        max_value = nums[-1]

        def solve_with_delta(delta):
            return solve_for_target(nums, cost1, cost2, max_value + delta, len(nums)) 

        result1 = solve_with_delta(0)
        result2 = solve_with_delta(23)
        results = [solve_with_delta(n) for n in range(24)]
        return min(results) % modulo





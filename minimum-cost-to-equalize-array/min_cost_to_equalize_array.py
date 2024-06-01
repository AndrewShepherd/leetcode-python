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




class Solution:
    def minCostToEqualizeArray(self, nums: list[int], cost1: int, cost2: int) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return (nums[1] - nums[0]) * cost1
        max_value = nums[-1]
        if cost1*2 <= cost2:
            return sum([max_value - n for n in nums]) * cost1
        
        calc = lambda target:calculate_cost(target, nums, cost1, cost2)
        def direction(target):
            result = [(t, calc(t)) for t in range(target, target + 200)]
            v1 = calc(target)
            v2 = calc(target + 1)
            return v1-v2

        l = max_value
        while(direction(l) > 0):
            l += 1
        return calc(l) % modulo

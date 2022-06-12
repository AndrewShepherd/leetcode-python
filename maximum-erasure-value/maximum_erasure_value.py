from itertools import accumulate

class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        accumulation = list(accumulate(nums))
        lastIndexes = dict()
        last_start_pos = 0
        max_value = 0
        for index, value in enumerate(nums):
            if value in lastIndexes:
                last_start_pos = max(last_start_pos, lastIndexes[value] + 1)
            sum_before = 0 if last_start_pos == 0 else accumulation[last_start_pos-1]
            sum_up_to = accumulation[index]
            current_sum = sum_up_to - sum_before
            max_value = max(max_value, current_sum)
            lastIndexes[value] = index
        return max_value
        
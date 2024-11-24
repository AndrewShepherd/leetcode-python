max_value = 10**9

class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        best_result = max_value
        for d in range(l, r+1):
            sub_arrays_start = range(len(nums)-d + 1)
            sub_arrays =[nums[s:s+d] for s in sub_arrays_start]
            sums = [sum(s) for s in sub_arrays]
            sums = [s for s in sums if s > 0]
            best_result = min([best_result] + sums)
        return best_result if best_result != max_value else -1

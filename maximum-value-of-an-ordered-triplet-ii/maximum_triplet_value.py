

class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        max_single = [None] * len(nums)
        min_single = [None] * len(nums)
        max_single[0] = nums[0]
        min_single[0] = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            max_single[i] = max(n, max_single[i-1])
            min_single[i] = min(n, min_single[i-1])
        max_sums = [None] * len(nums)
        min_sums = [None] * len(nums)
        max_sums[1] = nums[0] - nums[1]
        min_sums[1] = nums[0] - nums[1]
        for i in range(2, len(nums)):
            n = nums[i]
            max_sums[i] = max(max_sums[i-1], max_single[i-1] - n)
            min_sums[i] = min(min_sums[i-1], min_single[i-1] - n)

        best_result = 0
        for i in range(len(nums)-1, 1, -1):
            n = nums[i]
            if n > 0:
                this_result = max_sums[i-1] * n
            else:
                this_result = min_sums[i-1] * n
            best_result = max(best_result, this_result)
        return best_result



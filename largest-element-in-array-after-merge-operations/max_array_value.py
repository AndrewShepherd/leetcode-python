class Solution:
    def maxArrayValue(self, nums: list[int]) -> int:
        max_sum = 0
        current_sum = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= current_sum:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum

                

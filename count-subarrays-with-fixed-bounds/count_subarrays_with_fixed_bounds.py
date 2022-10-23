class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        range_start = 0
        max_min_index = -1
        max_max_index = -1
        count = 0
        for i,n in enumerate(nums):
            if n < minK or n > maxK:
                range_start = i + 1
            if n == minK:
                max_min_index = i
            if n == maxK:
                max_max_index = i
            max_start_pos = min(max_min_index, max_max_index)
            if max_start_pos >= range_start:
                count += max_start_pos - range_start + 1
        return count
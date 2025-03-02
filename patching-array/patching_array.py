class Solution:
    def minPatches(self, nums: list[int], target: int) -> int:
        patches = 0
        gap_start = 1
        index = 0
        while index < len(nums):
            n = nums[index]
            if n > gap_start:
                patches += 1
                gap_start += gap_start
            else:
                gap_start += n
                index += 1
            if gap_start > target:
                break
        while (gap_start <= target):
            gap_start += gap_start
            patches += 1
        return patches

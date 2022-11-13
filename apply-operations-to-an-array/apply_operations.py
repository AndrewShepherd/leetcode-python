class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        write_index = 0
        for i,v in enumerate(nums):
            if v != 0:
                nums[write_index] = v
                write_index += 1
        for i in range(write_index, len(nums)):
            nums[i] = 0
        return nums

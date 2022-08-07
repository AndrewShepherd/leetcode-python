def inPlaceSort(nums, startIndex, endIndexExclusive):
    for i in range(startIndex, endIndexExclusive-1):
        for j in range(i+1, endIndexExclusive):
            while j > i and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1],nums[j]
                j -= 1

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums)-2
        while nums[i] >= nums[i+1] and i >= 0:
            i -= 1
        if i < 0:
            nums.sort()
            return
        minNumber, minIndex = nums[i+1], i+1
        for j in range(i+1, len(nums)):
            if nums[j] < minNumber and nums[j] > nums[i]:
                minNumber, minIndex = nums[j], j
        nums[i], nums[minIndex] = nums[minIndex],nums[i]
        inPlaceSort(nums, i+1, len(nums))
        
        
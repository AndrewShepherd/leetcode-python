class Solution:
    def partitionArray(self, nums, k):
        count = 1
        nums.sort()
        partitionMin = nums[0]
        for index in range(1,len(nums)):
            v = nums[index]
            if v - partitionMin > k:
                partitionMin = v
                count += 1
        return count

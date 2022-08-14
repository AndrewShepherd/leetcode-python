class Solution:
    def validPartition(self, nums) -> bool:
        valid = [False] * len(nums) + [True, True]
        valid[-4] = (nums[-2] == nums[-1])
        for i in range(len(nums)-3,-1,-1):
            isValid2Ahead = valid[i+2]
            isValid3Ahead = valid[i+3]
            fits1 = nums[i] == nums[i+1]
            fits2 = fits1 and nums[i] == nums[i+2]
            fits3 = nums[i+1] == nums[i]+1 and nums[i+2] == nums[i] + 2
            valid[i] = (isValid2Ahead and fits1)
            valid[i] |= isValid3Ahead and fits2
            valid[i] |= isValid3Ahead and fits3
        return valid[0]
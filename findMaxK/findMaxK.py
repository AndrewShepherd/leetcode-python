class Solution:
    def findMaxK(self, nums) -> int:
        nums.sort()
        l = 0
        r = len(nums) -1
        while(l < r):
            nL, nR = nums[l], nums[r]
            if nL > 0:
                break
            elif nR < 0:
                break
            elif nL == 0 - nR:
                return nR
            elif abs(nL) > abs(nR):
                l += 1
            else:
                r -= 1
        return -1

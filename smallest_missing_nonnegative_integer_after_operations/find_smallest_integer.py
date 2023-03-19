class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        counts = [0] * value
        for n in nums:
            counts[n%value] += 1
        
        i = 0
        while(True):
            iMod = i % value
            if (counts[iMod] == 0):
                return i
            counts[iMod] -= 1
            i = i + 1

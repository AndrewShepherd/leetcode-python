class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        l = []
        r = []
        
        left = True
        l = nums[:1]
        r = nums[1:2]
        for n in nums[2:]:
            if l[-1] > r[-1]:
                l.append(n)
            else:
                r.append(n)
        return l + r
            

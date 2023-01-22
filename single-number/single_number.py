class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x,y = 0,0
        for n in nums:
            x, y = (~n & x) | (n & y), (~n & y) | (n & ~(x|y))
        return y

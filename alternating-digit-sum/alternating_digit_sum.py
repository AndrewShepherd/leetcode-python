class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        t = 0
        for d in [int(c) for c in str(n)]:
            t += d * sign
            sign *= -1
        return t
        

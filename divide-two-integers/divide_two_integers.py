class Solution(object):
    def divide(self, dividend, divisor):

        isNegative = (dividend < 0 ) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        t = 0
        m = 1
        while(divisor << 1 <= dividend):
            divisor <<= 1
            m <<= 1
        while dividend and m:
            if(dividend >= divisor):
                dividend -= divisor
                t += m
            divisor >>= 1
            m >>= 1
        
        if isNegative:
            t = max(
                0 - (1<<31),
                0 - t
            )
        else:
            t = min(
                (1 << 31) - 1,
                t
            )
        return t
        
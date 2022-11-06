def digitSum(n):
    s = 0
    while(n):
        s += n%10
        n //= 10
    return s

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        m = 1
        t = 0
        while(digitSum(n) > target):
            if n%10:
                t += (10 - n%10) * m
                n += 10
            m *= 10
            n = n//10
        return t

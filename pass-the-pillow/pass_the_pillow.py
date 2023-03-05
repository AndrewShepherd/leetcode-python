class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = 1
        d = 1
        while(time):
            p += d
            if p == n:
                d = -1
            elif p == 1:
                d = 1
            time -= 1
        return p

from math import comb

m = 10**9+7

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = abs(endPos - startPos)
        if diff%2 != k%2:
            return 0

        v1 = (k+diff)//2
        v2 = k-v1

        if v2 < 0:
            return 0
            
        return comb(v1+v2, v2) % m


import math

class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        l = math.inf
        r = 0-math.inf
        for n in nums:
            l = min(l, n)
            r = max(r, n)
        while r > l:
            m = (r + l)//2
            c = 0
            toggle = False
            for n in nums:
                if not toggle and n <= m:
                    c += 1
                    if c == k:
                        break
                    toggle = True
                else:
                    toggle = False
            l,r = (l,m) if c == k else (m+1,r)
        return l

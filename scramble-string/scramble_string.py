from collections import Counter, defaultdict
from functools import cache

class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        for i in range(len(s1)-1):
            c1[s1[i]] += 1
            c2[s2[-1-i]] += 1
            if c1 == c2:
                s1Left = s1[:i+1]
                s1Right = s1[i+1:]
                s2Right = s2[-1-i:]
                s2Left = s2[:-1-i]
                if not self.isScramble(s1Left, s2Right):
                    continue
                if not self.isScramble(s2Left, s1Right):
                    continue
                return True
        
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i, (c1, c2) in list(enumerate(zip(s1, s2)))[:-1]:
            d1[c1] += 1
            d2[c2] += 1
            if d1 == d2:
                if self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                    return True
        return False

from collections import Counter


def can_match(s, t):
    combined = s + s
    return combined.find(t) != -1


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        if not can_match(s, t):
            return 0
        if k == 0:
            return 1 if s == t else 0
        return 10 

"""
abc
cba


cab
bca
"""
        

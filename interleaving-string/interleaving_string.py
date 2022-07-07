from functools import cache

@cache
def canInterleave(s1, s2, target):
    if not s1:
        return s2 == target
    elif not s2:
        return s1 == target
    else:
        if s1[0] == target[0] and canInterleave(s1[1:], s2,target[1:]):
            return True
        else:
            return s2[0] == target[0] and canInterleave(s2[1:],s1,target[1:])
            

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return canInterleave(s1, s2, s3)
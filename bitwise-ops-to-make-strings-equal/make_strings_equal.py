def countZerosAndOnes(s):
    zeros, ones = 0, 0
    for c in s:
        if c == '0':
            zeros += 1
        else:
            ones += 1
    return (zeros, ones)

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        zBefore, oBefore = countZerosAndOnes(s)
        zTarget, oTarget = countZerosAndOnes(target)
        if (zBefore, oBefore) == (zTarget, oTarget):
            return True
        if not oTarget:
            return False
        if not oBefore:
            return False
        return True

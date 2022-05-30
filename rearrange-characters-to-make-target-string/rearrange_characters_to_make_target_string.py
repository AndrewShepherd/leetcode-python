from collections import Counter

class Solution(object):
    def rearrangeCharacters(self, s, target):
        counterS = Counter(s)
        counterT = Counter(target)

        return min(
            [counterS.get(k, 0)//counterT[k] for k in counterT]
        )

from collections import Counter

def splitIntoContiguousGroups(valuesAndCounts):
    groupStart = 0
    for i in range(1, len(valuesAndCounts)):
        if valuesAndCounts[i][0] - valuesAndCounts[i-1][0] > 1:
            yield valuesAndCounts[groupStart:i]
            groupStart = i
    yield valuesAndCounts[groupStart:]

class Solution:
    def isPossible(self, nums) -> bool:
        c = Counter(nums)
        l = sorted(c.items())
        for g in splitIntoContiguousGroups(l):
            if len(g) < 3:
                return False
            counts = [i[1] for i in g]
            s1 = 0
            s2 = 0
            s3 = 0
            for c in counts:
                if c < (s1+s2):
                    return False
                c -= (s1+s2)
                amountWeCanAllocateToS3 = min(c, s3)
                s3 = amountWeCanAllocateToS3 + s2
                s2 = s1
                s1 = c - amountWeCanAllocateToS3

        return s1 == 0 and s2 == 0

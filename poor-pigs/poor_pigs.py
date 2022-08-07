from math import ceil, comb

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets <= 1:
            return 0
        allowedTurns = ceil(minutesToTest/minutesToDie)
        # Each entry represents the maximum buckets that can be searched with (index+1 pigs)
        # given the turn
        maximumBuckets = [1]*(buckets+1)
        for turn in range(allowedTurns):
            mb2 = maximumBuckets[:]
            for i in range(1, len(maximumBuckets)):
                mb2[i] = sum([comb(i, i-j)*maximumBuckets[i-j] for j in range(i+1)])
                if(mb2[i]>=buckets):
                    break # No need to keep calculating!
            maximumBuckets = mb2
        return i
            
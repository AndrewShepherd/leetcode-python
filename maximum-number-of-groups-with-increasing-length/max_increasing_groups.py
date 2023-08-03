import heapq

class Solution:
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        if (min(usageLimits) >= len(usageLimits)):
            return len(usageLimits)
        
        usageLimits.sort()
        for i in range(len(usageLimits)):
            usageLimits[i] = min(usageLimits[i], i+1)

        levels = [0] * (len(usageLimits) + 1)
        current_level = 0
        levels[0] = len(usageLimits)
        last_level_hit = 0
        for n in enumerate(reversed(usageLimits)):
            # we have to get level[last_level_hit+1] at  
            target_level = last_level_hit + 1
            target_index = last_level_hit
            j = 0
            while levels[j] > target_index:
                j += 1
            

        return 0
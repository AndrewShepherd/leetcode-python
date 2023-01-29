import math
from functools import cache

class Solution:

    def putMarbles(self, weights: list[int], k: int) -> int:

        dp_lengths = len(weights)-k+1
        start_val = (math.inf, -math.inf)
        dp = [start_val] * dp_lengths
        for i in range(len(dp)):
            score = weights[0] + weights[i]
            dp[i] = (score, score)
        
        for offset in range(1, k):
            dp2 = [start_val] * dp_lengths
            for i in range(len(dp2)):
                best_min, best_max = start_val
                for j in range(i+1):
                    prev_min, prev_max = dp[j]
                    this_start, this_end = (weights[j + offset], weights[i + offset])
                    this_val = this_start + this_end
                    this_min = prev_min + this_val
                    this_max = prev_max + this_val
                    best_min = min(best_min, this_min)
                    best_max = max(best_max, this_max)
                dp2[i] = (best_min, best_max)
            dp = dp2
        l,r = dp[-1]
        return r - l


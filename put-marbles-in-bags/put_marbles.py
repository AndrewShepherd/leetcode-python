import math

class Solution:

    def putMarbles(self, weights: list[int], k: int) -> int:
        dp_lengths = len(weights)-k+1
        dp = [None] * dp_lengths
        for i in range(len(dp)):
            score = weights[0] + weights[i]
            dp[i] = (score, score)        
        for offset in range(1, k):
            dp2 = [None] * dp_lengths
            min_start = math.inf
            max_start = -math.inf
            for i in range(len(dp2)):
                prev_min, prev_max = dp[i]
                this_end = weights[i + offset]
                min_start = min(min_start, prev_min + this_end)
                max_start = max(max_start, prev_max + this_end)
                dp2[i] = (min_start + this_end , max_start + this_end)
            dp = dp2
        l,r = dp[-1]
        return r - l


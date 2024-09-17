import math

class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        dp = [0] * len(b)
        # A[0]
        for i,v in enumerate(b):
            if i == 0:
                dp[i] = v * a[0]
            else:
                dp[i] = max(dp[i-1], v*a[0])
        # A[1]
        for a_index in range(1, len(a)):
            dp2 = [0] * len(b)
            for i in range(a_index, len(b)):
                v = b[i]
                # included value
                included_value = v * a[a_index] + dp[i-1]
                if i == a_index:
                    dp2[i] = included_value
                else:
                    dp2[i] = max(included_value, dp2[i-1])
            dp = dp2
        return dp[-1]

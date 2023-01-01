class Solution:
    def minCut(self, s: str) -> int:
        dp = [-1] * (len(s)+1)

        for i in range(1, len(s)+1):
            this_result = len(s)
            for j in range(i):
                substr = s[j:i]
                if substr == substr[::-1]:
                    this_count =  dp[j] + 1
                    this_result = min(this_result, this_count)
            dp[i] = this_result

        return dp[-1]


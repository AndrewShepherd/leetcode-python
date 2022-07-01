

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # DP = smallest number with a length of i
        dp = [0]
        for c in reversed(s):
            thisDigit = 0 if c == '0' else 1
            if thisDigit == 0:
                dp = [0] + dp
            else:
                dp.append(dp[-1] + 2**(len(dp)-1))
        for i in range(len(dp)-1, -1, -1):
            if dp[i] <= k:
                return i

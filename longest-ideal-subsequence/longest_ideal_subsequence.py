class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        s = list(reversed([ord(c)-ord('a') for c in s]))
        dp = [0]*26
        for n in s:
            dp2 = dp[:]
            dp2[n] = 1 + max(dp[max(0,n-k):n+k+1])
            dp = dp2
        return max(dp)
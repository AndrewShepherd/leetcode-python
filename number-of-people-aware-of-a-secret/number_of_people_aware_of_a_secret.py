class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [1] + [0] * (forget-1)
        for i in range(n-1):
            dp = [0] + dp[:-1]
            dp[0] = sum(dp[delay:])
        return sum(dp) % 1000000007

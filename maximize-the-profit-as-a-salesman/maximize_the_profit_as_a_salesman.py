class Solution:
    def maximizeTheProfit(self, n: int, offers: list[list[int]]) -> int:
        dp = [0] * (n+1)
        offers.sort(key = lambda o:o[1])
        last_populated_index = -1
        for start,end_inclusive,price in offers:
            while last_populated_index < end_inclusive:
                last_populated_index += 1
                if last_populated_index != 0:
                    dp[last_populated_index] = dp[last_populated_index-1]
            dp[end_inclusive] = max(dp[end_inclusive], dp[start-1] + price)
        return dp[end_inclusive]

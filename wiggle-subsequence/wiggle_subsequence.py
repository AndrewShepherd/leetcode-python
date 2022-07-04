class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if not nums:
            return 0
        dp = [(0, 0)] * (max(nums)+1)
        for n in nums:
            dp[n] = (
                max(
                    dp[n][0],
                    (max([e[1] for e in dp[n+1:]]) if n < len(dp)-1 else 0) + 1
                ),
                max(
                    dp[n][1],
                    (max([e[0] for e in dp[:n]]) if n > 0 else 0) + 1
                )
            )
        return max(max(e) for e in dp)

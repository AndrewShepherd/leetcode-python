modulo = 1000000007

class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for count, marks in types:
            dp2 = dp[:]
            for i in range(marks, len(dp2)):
                for j in range(1, count+1):
                    p = i - marks*j
                    if p < 0:
                        break
                    dp2[i] = (dp2[i] + dp[p]) % modulo
            dp = dp2
        return dp[-1]

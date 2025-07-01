class Solution:
    def findCoins(self, numWays: list[int]) -> list[int]:
        availableValues = []
        dp = [0] * (len(numWays) + 1)
        dp[0] = 1
        for i, n in enumerate(numWays):
            target = i + 1
            
            expected_result = dp[target]
            
            if n < expected_result:
                return []
            elif n == expected_result:
                continue
            elif n == expected_result + 1:
                availableValues.append(target)
                dp2 = dp[:]
                for m in range(target, len(dp2), target):
                    for j in range(m, len(dp2)):
                        dp2[j] += dp[j - m]
                dp = dp2
            else:
                return []
        
        return availableValues

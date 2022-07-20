
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        dp = [1] * maxValue
        for _ in range(1,n):
            dp2 = [1] * maxValue
            for i in range(len(dp)):
                subTotal = sum(dp[i::i+1])
                if(subTotal == 1):
                    break
""                dp2[i] = subTotal % 1000000007
                
            dp = dp2
        return sum(dp) % 1000000007
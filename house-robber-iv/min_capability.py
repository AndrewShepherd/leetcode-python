import math

class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:

        #k = (l + 1)/2
        # 2*k = l+1
        #

        two_behind = [nums[0]] + [math.inf]*(k-1)
        one_behind = [min(nums[0:2])] + [math.inf]*(k-1)

        for i in range(2, len(nums)):
            n = nums[i]
            dp = two_behind[:]
            j = min(k-1, i//2)
            while(j > 0):
                this_value = max(two_behind[j-1], n)
                if this_value == math.inf:
                    raise "How did that happen?"
                if this_value >= two_behind[j]:
                    break
                dp[j] = this_value
                j -= 1
            dp[0] = min(two_behind[0], n)

            two_behind = [min(l,r) for l,r in zip(one_behind, two_behind)]
            one_behind = dp
        return min(two_behind[-1], one_behind[-1])

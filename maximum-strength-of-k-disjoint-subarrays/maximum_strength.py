from array import array

class Solution:
    def maximumStrength(self, nums: list[int], k_total: int) -> int:
        dp_length = len(nums) - k_total + 1
        dp = [0] * dp_length
        dp_prev = [0] * dp_length
        for k in range(k_total):
            source_index = k
            dp_prev, dp = dp, dp_prev
            s = -1 if k%2 else 1
            m = (k_total - k)
            n = nums[k] * m * s
            last_selected = dp_prev[0] + n
            dp[0] = last_selected
            for i in range(1, dp_length):
                source_index = i + k
                n = nums[source_index] * m * s
                last_selected = max(last_selected + n, dp_prev[i] + n)
                dp[i] = max(last_selected, dp[i-1])
        return dp[-1]
MODULO = 10**9 + 7

class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        max_value = max(nums)
        # dp = number of options if min(descending) == i
        dp = [0] * (max_value + 1)

        last_num = nums[-1]

        for i,v in enumerate(range(last_num+1, 0, -1)):
            dp[i] = v

        for nums_index in range(len(nums)-2, -1, -1):
            dp2 = [0] * (max_value + 1)
            offset = max(nums[nums_index+1] - nums[nums_index], 0)
            for dp_index in range(nums[nums_index], -1, -1):
                to_the_right = dp[dp_index + offset] if dp_index + offset < len(dp) else 0
                above = dp2[dp_index + 1] if dp_index + 1 < len(dp2) else 0
                dp2[dp_index] = (to_the_right + above) % MODULO
            dp = dp2
        return dp[0]

class Solution:
    def maximumStrength(self, nums: list[int], k_total: int) -> int:
        dp_any_range = [0] * len(nums)

        # solve it for 1
        last_selected = nums[0] * k_total
        dp_any_range[0] = last_selected
        for i in range(1, len(nums)):
            n = nums[i] * k_total
            last_selected = max(last_selected + n, n)
            dp_any_range[i] = max(last_selected, dp_any_range[i-1])

        # solve it for the rest
        for k in range(1, k_total):
            s = -1 if k%2 else 1
            m = (k_total - k)
            n = nums[k] * m * s
            
            dp_any_range_prev = dp_any_range
            dp_any_range = [0] * len(nums)
            last_selected = dp_any_range_prev[k-1] + n
            dp_any_range[k] = last_selected
            for i in range(k+1, len(nums)):
                n = nums[i] * m * s
                last_selected = max(last_selected + n, dp_any_range_prev[i-1] + n)
                dp_any_range[i] = max(last_selected, dp_any_range[i-1])

        return dp_any_range[-1]
        
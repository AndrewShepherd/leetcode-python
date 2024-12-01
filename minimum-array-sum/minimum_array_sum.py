from math import inf

class Solution:
    def minArraySum(self, nums: list[int], k: int, op1: int, op2: int) -> int:
        apply_op1 = lambda n: (n+1)//2
        apply_op2 = lambda n: (n - k) if n >= k else n
        apply_both = lambda n: min(apply_op1(apply_op2(n)), apply_op2(apply_op1(n)))

        make_dp = lambda : [[inf] * (op2+1) for _ in range(op1+1)]

        dp = make_dp()
        dp[0][0] = 0
        for n in nums:
            transforms = [
                (n, 0, 0),
                (apply_op1(n), 1, 0),
                (apply_op2(n), 0, 1),
                (apply_both(n), 1, 1)
            ]
            dp2 = make_dp()
            for row_index, row in enumerate(dp):
                if row[0] == inf:
                    break
                for col_index, value in enumerate(row):
                    if value == inf:
                        break
                    for t, dr, dc in transforms:
                        target_row = row_index + dr
                        if target_row >= len(dp):
                            continue
                        target_col = col_index + dc
                        if target_col >= len(row):
                            continue
                        dp2[target_row][target_col] = min(
                                dp2[target_row][target_col], 
                                value + t
                            )
            dp = dp2
        return dp[-1][-1]
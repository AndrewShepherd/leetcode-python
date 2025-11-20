from functools import cache
from math import inf;


start_as_max = 0
start_as_min = 1
finish_partition = 2

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
       
        def best_result(range_start, range_length, available_partitions):
            if (available_partitions == 0):
                return 0
            if range_length < 2:
                return 0
            range_start %= len(nums)
            dp = [
                [-inf, -inf, 0] for i in range(k)
            ]
            for i in range(range_length):
                n = nums[(range_start + i)% len(nums)]
                dp2 = [None] * k
                for j in range(len(dp)):
                    this_entry = dp[j]
                    previous_entry = None if j == 0 else dp[j-1]
                    if previous_entry == None:
                        dp2[j] = [
                            max(n, this_entry[start_as_max]),
                            max(0 - n, this_entry[start_as_min]),
                            max(
                                this_entry[finish_partition],
                                this_entry[start_as_max] - n,
                                this_entry[start_as_min] + n
                            )
                        ]
                    else:
                        dp2[j] = [
                            max(previous_entry[finish_partition] + n, this_entry[start_as_max]),
                            max(previous_entry[finish_partition] - n, this_entry[start_as_min]),
                            max(
                                this_entry[finish_partition],
                                this_entry[start_as_max] - n,
                                this_entry[start_as_min] + n
                            )
                        ]
                dp = dp2
            return max([e[finish_partition] for e in dp])

        result = 0
        _, max_index = max([(v,i) for i,v in enumerate(nums)])
        return max(
            best_result(max_index, len(nums), k), 
            best_result(max_index + 1, len(nums), k)
        )


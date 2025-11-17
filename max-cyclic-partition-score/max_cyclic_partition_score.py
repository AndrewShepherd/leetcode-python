from functools import cache


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        @cache 
        def best_result(array_start, this_partition_start, available_partitions):
            if (available_partitions == 0):
                return 0
            partition_length = 1
            i = this_partition_start
            min_value = nums[i]
            max_value = nums[i]
            result = 0
            best_result_for_this_only = 0
            while (True):
                i = (i+1)%len(nums)
                if i == array_start:
                    break
                min_value = min(min_value, nums[i])
                max_value = max(max_value, nums[i])
                diff = max_value - min_value
                if diff > best_result_for_this_only:
                    best_result_for_this_only = diff
                    if (i+1)%len(nums) != array_start:
                        result = max(
                            result, 
                            diff + best_result(array_start, (i+1)%len(nums), available_partitions-1)
                        )
                    else:
                        result = max(result, diff)
            return result

        result = 0
        for i in range(len(nums)):
            result = max(result, best_result(i, i, k))
        return result

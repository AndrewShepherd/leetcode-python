from functools import cache


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
       
        @cache 
        def best_result(range_start, range_length, available_partitions):
            if (available_partitions == 0):
                return 0
            if range_length < 2:
                return 0
            range_start %= len(nums)
            max_so_far = nums[range_start]
            min_so_far = nums[range_start]
            biggest_range = 0
            result =  0
            for i in range(1, range_length):
                index = (range_start + i) % len(nums)
                max_so_far = max(max_so_far, nums[index])
                min_so_far = min(min_so_far, nums[index])
                this_range = max_so_far - min_so_far
                if (this_range > biggest_range):
                    biggest_range = this_range
                    if available_partitions > 0:
                        all_the_rest = best_result(index + 1, range_length - i - 1, available_partitions - 1)
                        result = max(result, biggest_range + all_the_rest)
                    else:
                        result = biggest_range
            return result

        result = 0
        _, max_index = max([(v,i) for i,v in enumerate(nums)])
        return max(
            best_result(max_index, len(nums), k), 
            best_result(max_index + 1, len(nums), k)
        )


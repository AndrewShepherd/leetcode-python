import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        total = 0
        all_zero_indexes = []
        continuous_ones_start = 0
        for i,c in enumerate(s):
            if c == '0':
                all_zero_indexes.append(i)
                continuous_ones = i - continuous_ones_start
                total += continuous_ones * (continuous_ones + 1) // 2
                continuous_ones_start = i + 1
        if (all_zero_indexes):
            continuous_ones = len(s) - all_zero_indexes[-1] - 1
        else:
            continuous_ones = len(s)
        total += continuous_ones * (continuous_ones + 1) // 2
        zero_counts = len(all_zero_indexes)
        zero_limit = min(zero_counts, math.floor(math.sqrt(len(s))))

        for z in range(1, zero_limit + 1):
            required_one_count = z*z
            base_required_window_size = z + required_one_count

            zero_index_range_start = 0
            zero_index_range_end = z
            range_start = 0
            range_end = all_zero_indexes[zero_index_range_end-1] + 1
            while (True):
                this_minimum_length = max(base_required_window_size, range_end - all_zero_indexes[zero_index_range_start])
                this_maximum_length = range_end - range_start
                if (this_maximum_length >= this_minimum_length):
                    total += max(this_maximum_length - this_minimum_length + 1, 0)
                if range_end == len(s):
                    break
                if s[range_end] == '0':
                    range_start = all_zero_indexes[zero_index_range_start] + 1
                    zero_index_range_start += 1
                    zero_index_range_end += 1
                range_end += 1
        return total

from math import inf

class Solution:
    def minXor(self, nums: list[int], k: int) -> int:
        max_length = len(nums) - k + 1
        grid = [[inf] * k for _ in range(len(nums))]

        # first index = number of elements used
        # second index = numer of groups
        for range_start in range(len(nums)):
            aggregate =0
            for range_length in range(1, min(len(nums)-range_start + 1, max_length+1)):
                aggregate ^= nums[range_start + range_length - 1]
                number_of_elements_used = range_start + range_length
                grid_row_index = number_of_elements_used - 1
                grid_row = grid[grid_row_index]
                source_row_index = range_start - 1
                if (source_row_index < 0):
                    grid_row[0] = aggregate
                else:
                    source_row = grid[source_row_index]
                    has_found_values = False
                    for i in range(1, k):
                        values_for_k_minus_one = source_row[i-1]
                        if (values_for_k_minus_one == inf):
                            if has_found_values:
                                break
                            else:
                                continue
                        has_found_values = True
                        this_candidate_value = max(values_for_k_minus_one, aggregate)
                        existing_value = grid_row[i]
                        grid_row[i] = min(existing_value, this_candidate_value)

        return grid[-1][-1]

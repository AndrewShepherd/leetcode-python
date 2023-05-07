class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        result = [0] * len(queries)
        nums = [0] * n

        def has_adjacent_same_color(nums_index):
            if not (0 <= nums_index < len(nums)):
                return False
            if nums[nums_index] == 0:
                return False
            color_before = None if nums_index == 0 else nums[nums_index - 1]
            color_after = None if nums_index == len(nums) - 1 else nums[nums_index + 1]
            return nums[nums_index] == nums[nums_index] == color_after
            #return nums[nums_index] == color_before or nums[nums_index] == color_after


        for query_index,(nums_index, color) in enumerate(queries):
            values_before = sum([1 if has_adjacent_same_color(i) else 0 for i in range(nums_index-1, nums_index+1)])
            nums[nums_index] = color
            values_after = sum([1 if has_adjacent_same_color(i) else 0 for i in range(nums_index-1, nums_index+1)])
            result[query_index] = (result[query_index-1] if query_index > 0 else 0) + values_after - values_before

        return result

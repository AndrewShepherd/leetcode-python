class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        bad_pair_starts = []
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                bad_pair_starts.append(i-1)
        result = []
        if not bad_pair_starts:
            return [True] * len(queries)
        
        def is_special(range_start, range_end_inclusive):
            search_start = 0
            search_end_exclusive = len(bad_pair_starts)
            while(search_end_exclusive > search_start):
                mid_index = (search_start + search_end_exclusive)//2
                mid_value = bad_pair_starts[mid_index]
                if range_start <= mid_value < range_end_inclusive:
                    return False
                elif mid_value < range_start:
                    search_start = mid_index + 1
                else:
                    search_end_exclusive = mid_index 
            return True    
        result = []
        for range_start, range_end_inclusive in queries:
            result.append(is_special(range_start, range_end_inclusive))
        return result

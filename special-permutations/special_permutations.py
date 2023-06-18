from functools import cache

MODULO = int(10**9 + 7)

class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        adjacencies = [[False] * len(nums) for _ in range(len(nums))]
        for i1,v1 in enumerate(nums):
            for i2 in range(i1+1, len(nums)):
                v2 = nums[i2]
                if v1%v2 == 0 or v2%v1 == 0:
                    adjacencies[i1][i2] = True
                    adjacencies[i2][i1] = True 

        def remove_element(t:tuple, n:int):
            index = t.index(n)
            return t[:index] + t[index+1:]

        @cache 
        def solve_recursive(available_nums:tuple[int], starting_from:tuple[int]) -> int:
            if len(available_nums) == 0:
                return 1
            total = 0
            for i,v in enumerate(starting_from):
                remaining = remove_element(available_nums, v)
                possible_next = tuple([n for n in remaining if adjacencies[v][n]])
                total = (total + solve_recursive(remaining, possible_next)) % MODULO
            return total
        range_as_tuple = tuple(range(len(nums)))
        return solve_recursive(range_as_tuple, range_as_tuple)

import math
from functools import cache
class Solution:
    def partitionString(self, s: str) -> int:
        


        if not s:
            return 0
        s = [ord(c) - ord('a') for c in s]

        @cache
        def solve_recursive(start_index, not_more_than = math.inf):
            if start_index >= len(s):
                return 0

            best_we_can_do = (len(s)-start_index+1)//26
            if best_we_can_do > not_more_than:
                return -1

            i = start_index
            letters = [0]*26
            while i < len(s) and letters[s[i]] == 0:
                letters[s[i]] = 1
                i += 1
        
            best_result = math.inf

            while i > start_index:
                this_result = solve_recursive(i, min(best_result-1, not_more_than-1))
                if this_result != -1:
                    best_result = min(best_result, this_result+1)
                i -= 1
            return best_result

        return solve_recursive(0)
from functools import cache

def possibleLengths(s: str, start: int) -> int:
    l = 1
    while start + l*2 <= len(s):
        if s[start : start + l] == s[start + l : start + l * 2]:
            yield l
        l += 1

class Solution:
    def deleteString(self, s: str) -> int:

        @cache
        def optimal_result(startIndex):
            best_result = 1
            for pl in possibleLengths(s, startIndex):
                best_possible_result = 1 + len(s) - startIndex - pl
                if best_possible_result <= best_result:
                    break
                this_result = 1 + optimal_result(startIndex + pl)
                best_result = max(best_result, this_result)
            return best_result
        
        # Populate the cache from the last index
        # to the first. (By doing it backwards,
        # we avoid the python recursion limit)
        for index in range(len(s) - 1, 0, -1):
            optimal_result(index)
        return optimal_result(0)


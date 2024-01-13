from functools import cache
import sys

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        s = [1 << (ord(c) - ord('a')) for c in s]

        sys.setrecursionlimit(max(1000, len(s)))
        @cache
        def brute_force_solve(index, one_substitution_left, current_set):
            if index == len(s):
                best_result = 1 if current_set else 0
            else:
                new_set = current_set | s[index]
                if new_set.bit_count() > k:
                    best_result = 1 + brute_force_solve(index + 1, one_substitution_left, s[index])
                else:
                    best_result = brute_force_solve(index + 1, one_substitution_left, new_set)
                
                if one_substitution_left:
                    for i in range(26):
                        mask = 1 << i
                        new_set = current_set | mask
                        if new_set.bit_count() > k:
                            best_result = max(best_result, 1 + brute_force_solve(index + 1, False, mask))
                        else:
                            best_result = max(best_result, brute_force_solve(index + 1, False, new_set))
            return best_result

        return brute_force_solve(0, True, 0)
        

from functools import cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        c = [s[0]]
        for i in range(1, len(s)):
            if s[i] != c[-1]:
                c.append(s[i])
        
        @cache
        def solve(start_index, end_exclusive_index, ambient_char):
            if end_exclusive_index == start_index:
                result = 0
            elif end_exclusive_index - start_index == 1:
                result = 0 if c[start_index] == ambient_char else 1
            elif c[start_index] == ambient_char:
                result = solve(start_index+1, end_exclusive_index, ambient_char)
            else:
                result = end_exclusive_index - start_index
                for cover_range in range(1, end_exclusive_index - start_index + 1):
                    if c[start_index + cover_range - 1] != c[start_index]:
                        continue
                    left_result = solve(
                        start_index,
                        start_index + cover_range, 
                        c[start_index]
                    )
                    right_result = solve(
                        start_index + cover_range, 
                        end_exclusive_index,
                        ambient_char
                    )
                    this_result = 1 + left_result + right_result
                    result = min(
                        result,
                        this_result
                    )
            return result

        return solve(0, len(c), None)

import math

class Solution:
    def maximumGroups(self, g) -> int:

        # (n^2 + n)/2 = g
        # (n^2 + n) = 2g
        # n^2 + n - 2g = 0

        # (-b + sqrt(b - 4ac)/2a) = n
        # (-1 + srt(1 + 8g)/2) = n
        # n = (sqrt(1 + 8g)-1)/2
        return int((math.sqrt(1 + 8*len(g))-1)/2)

        grades = sorted(grades)
        c = 0
        min_length = 1
        min_value = 1
        while grades:
            range_end = min_length
            if range_end > len(grades):
                return c
            while sum(grades[:range_end]) < min_value:
                range_end += 1
                if range_end > len(grades):
                    return c
            c += 1
            min_length = range_end + 1
            min_value = sum(grades[:range_end]) + 1
            grades = grades[range_end:]
        return c
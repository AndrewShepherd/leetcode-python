from functools import cache

def calculate_diff(n1, n2):
    return min([abs(n1 - n2), abs(n1 + 26 - n2), abs(n1 - (n2 + 26))])

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        s = [ord(c) - ord('a') for c in s]

        @cache 
        def solve(start_index, length, available_actions):
            if (length < 1):
                return 0
            if (length == 1):
                return 1
            max_without_including_start = solve(start_index + 1, length-1, available_actions)
            max_without_including_last = solve(start_index, length-1, available_actions)
            diff = calculate_diff(s[start_index],  s[start_index + length-1])
            max_including_both = 0
            if (diff <= available_actions):
                max_including_both = 2 + solve(start_index + 1, length-2, available_actions- diff)
            return max([max_without_including_start, max_without_including_last, max_including_both])

        return solve(0, len(s), k)


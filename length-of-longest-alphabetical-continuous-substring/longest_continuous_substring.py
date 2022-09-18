class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        length = 1
        max_length = 1
        s = [ord(c) for c in s]
        for i in range(1, len(s)):
            if s[i] - s[i-1] == 1:
                length += 1
            else:
                length = 1
            max_length = max(max_length, length)
        return max_length

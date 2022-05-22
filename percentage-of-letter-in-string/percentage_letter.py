class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        count = sum(1 if c == letter else 0 for c in s)
        return count * 100 // len(s)
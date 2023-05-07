

class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        return s[:-1] + chr(ord(s[-1] + 1))

from collections import defaultdict

class Solution:
    def greatestLetter(self, s: str) -> str:
        d = defaultdict(lambda: (False, False))
        for c in s:
            current = d[c.upper()]
            if c.isupper():
                current = (True, current[1])
            else:
                current = (current[0], True)
            d[c.upper()] = current
        allChars = sorted(d.keys())
        for c in reversed(allChars):
            hasUpper, hasLower = d[c.upper()]
            if (hasUpper and hasLower):
                return c
        return ""
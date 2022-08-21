from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        highestSingle = None
        itemsAndCounts = sorted(c.items(), key=lambda ch:0-ord(ch[0]))

        left = ""
        for ch, n in itemsAndCounts:
            if (not left) and (ch == '0'):
                if highestSingle == None:
                    highestSingle = ch
            else:
                left += ch*(n//2)
                if n%2 == 1 and highestSingle == None:
                    highestSingle = ch
        result = left
        if highestSingle:
            result += highestSingle
        result += left[::-1]
        return result
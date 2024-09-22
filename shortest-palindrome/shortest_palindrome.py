class Solution:    
    def shortestPalindrome(self, s: str) -> str:
        lps = [0] * len(s)
        l = 0
        i = 1
        while (i < len(s)):
            if s[i] == s[l]:
                l += 1
                lps[i] = l
                i += 1
            elif l == 0:
                i += 1
            else:
                l = lps[l-1]

        l = 0
        i = len(s) - 1
        while (i >= 0):
            if s[i] == s[l]:
                l += 1
                i -= 1
            elif l == 0:
                i -= 1
            else:
                l = lps[l-1]
        # l is the length of the palindrom
        prefix = s[:l-1:-1]
        return prefix + s

        

            


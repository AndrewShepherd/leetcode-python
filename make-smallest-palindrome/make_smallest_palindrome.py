class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)
        l = 0
        r = len(a) -1
        while(l < r):
            if a[l] == a[r]:
                None
            elif a[l] < a[r]:
                a[r] = a[l]
            else:
                a[l] = a[r]
            l += 1
            r -= 1
        return ''.join(a)
